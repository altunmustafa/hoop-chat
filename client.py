# -*- coding: utf-8 -*-
import sys
import socket
import threading
import logging
from PyQt4 import QtGui, QtCore
from mainwindow import Ui_MainWindow
from accountDialog import Ui_accountDialog
from addFriend import Ui_addFriend
from chatDialog import Ui_chatDialog
from registerDialog import Ui_registerDialog

HOST = "192.168.137.27"
PORT = 1220
BUF_SIZE = 1024

global check_error
check_error = 0

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    logging.info("Kritik Hata İçsel bir hata ile karşılaşıldı.")
    sys.exit(1)

try:
    socket.connect((HOST, PORT))
except:
    check_error = 3006

class registerDialog(QtGui.QDialog, Ui_registerDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_registerDialog()
        self.ui.setupUi(self)

        self.connect(self.ui.reg_submit, QtCore.SIGNAL("pressed()"), self.send_register_request)
        self.connect(self.ui.reg_exit, QtCore.SIGNAL("pressed()"), self.exit_register_dialog)

    def send_register_request(self):
        self.reg_username = self.ui.reg_usernameBox.text()
        self.reg_password = self.ui.reg_passwordBox.text()
        self.reg_credentials = self.reg_username + " " + self.reg_password

        socket.send("#" + self.reg_credentials)
        mysql_response = socket.recv(BUF_SIZE)

        if mysql_response == "2003":
            QtGui.QMessageBox.information(self, u"Başarılı", u"Kullanıcı başarıyla oluşturuldu")
        elif mysql_response == "3003":
            QtGui.QMessageBox.warning(self, u"Başarısız", u"Kullanıcı adı kullanılıyor")

    def exit_register_dialog(self):
        self.close()

class addFriendDialog(QtGui.QDialog, Ui_addFriend):
    def __init__(self,account_dialog):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_addFriend()
        self.ui.setupUi(self)
        self.account_dialog=account_dialog

        self.connect(self.ui.addFriendExit, QtCore.SIGNAL("pressed()"), self.exit_friend_dialog)
        self.connect(self.ui.addFriendSubmit, QtCore.SIGNAL("pressed()"), self.add_friend_submit)

    def add_friend_submit(self):
        self.friend_uname = self.ui.friend_uname.text()
        socket.send("!" + self.friend_uname)
        self.account_dialog.new_friend(self.friend_uname)

    def exit_friend_dialog(self):
        self.close()

class chatDialog(QtGui.QMainWindow, Ui_chatDialog):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_chatDialog()
        self.ui.setupUi(self)

        self.connect(self.ui.lineEdit, QtCore.SIGNAL("returnPressed()"), self.send_msg)

    def send_msg(self):
        send_msg = self.ui.lineEdit.text()
        socket.send(self.ui.chattingFriend.text() + "-" + send_msg)
        self.ui.lineEdit.clear()
        self.ui.textBrowser.append("Ben: " + send_msg)

class accountDialog(QtGui.QMainWindow, Ui_accountDialog):
    def __init__(self, username, my_friends):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_accountDialog()
        self.ui.setupUi(self)
        self.username = username
        self.i = 0
        self.chat_dialog = [ chatDialog() for i in range(10) ]
        self.my_friends = my_friends

        self.connect(self.ui.actionAdd_Friend, QtCore.SIGNAL("triggered()"), self.add_friend)

        while True:
            my_friend = my_friends.split("$")[0]
            my_friends = my_friends.split("$", 1)[1]
            if my_friend != "":
                self.ui.listWidget.addItem(my_friend)
            if my_friends == "":
                break

        self.ui.listWidget.itemDoubleClicked.connect(self.chat_with_friend)

    def new_friend(self, new_friend):
        self.ui.listWidget.addItem(new_friend)

    def add_friend(self):
        self.add_friend_dialog = addFriendDialog(self)
        self.add_friend_dialog.show()

    def chat_with_friend(self):
        self.chat_dialog[self.i].ui.chattingFriend.setText(self.ui.listWidget.currentItem().text())
        self.chat_dialog[self.i].show()
        self.i = self.i + 1

    def get_message(self, msg):
        from_user = strip_non_ascii(msg.split("-")[0])
        msg = msg.split("-")[1]
        isOpen = 0

        for i in range(0, 10):
            if self.chat_dialog[i].ui.chattingFriend.text() == from_user:
                isOpen = 1
                self.chat_dialog[i].ui.textBrowser.append(from_user + ": " + msg)

        if not isOpen:
            for i in range(0, 10):
                if self.chat_dialog[i].ui.chattingFriend.text() == "TextLabel":
                    self.chat_dialog[i].ui.chattingFriend.setText(from_user)
                    self.chat_dialog[i].show()
                    self.chat_dialog[i].ui.textBrowser.append(from_user + ": " + msg)
                    break

class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect(self.ui.exitButton, QtCore.SIGNAL("pressed()"), self.exit_app)
        self.connect(self.ui.action_exit, QtCore.SIGNAL("triggered()"), self.exit_app)
        self.connect(self.ui.loginButton, QtCore.SIGNAL("pressed()"), self.login)
        self.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.about_hoop)
        self.connect(self.ui.actionTeam, QtCore.SIGNAL("triggered()"), self.about_team)
        self.ui.kayit_ol.mousePressEvent = self.register
        self.ui.kayit_ol.setStyleSheet("QLabel { color:Teal; font-weight:bold;}")

    def about_team(self):
        QtGui.QMessageBox.about(self, u"Ekip", u"\nMustafa ALTUN (314005)\nEmre ÖZEL (314037)\nAbdullah ÇAY (314039)\t\t\t")

    def about_hoop(self):
        QtGui.QMessageBox.about(self, u"Hoop Chat", u"Hoop chat arkadaşlarınızla hızlı ve pratik iletişim kurmanızı sağlar.")

    def register(self, event):
        self.register_dialog = registerDialog()
        self.register_dialog.show()

    def exit_app(self):
        QtCore.QCoreApplication.exit()
        socket.close()

    def login(self):
        if check_error == 3006:
            QtGui.QMessageBox.warning(self, u"Bağlantı Hatası", u"Bağlantı ayarlarınızı kontrol edin")

        self.username = self.ui.usernameBox.text()
        self.password = self.ui.passBox.text()
        self.credentials = self.username + " " + self.password
        socket.send("$" + self.credentials)

        self.response = socket.recv(BUF_SIZE)
        self.response = strip_non_ascii(self.response)

        if self.response[:3] == "ACK":
            my_friends = self.response.split("$$", 1)[1]
            self.hide()
            self.account_dialog = accountDialog(self.username, my_friends)
            self.account_dialog.show()
            recv = Recv(self.account_dialog)
            recv.start()
        elif self.response[:3] == "RST":
            QtGui.QMessageBox.warning(self, u"Başarısız", u"Kullanıcı adı veya şifre hatalı. Lütfen tekrar deneyin.")

class Recv(threading.Thread):
    def __init__(self,account_Dialog):
        threading.Thread.__init__(self)
        self.account_dialog = account_Dialog

    def run(self):
        while 1:
            buf = socket.recv(BUF_SIZE)
            self.account_dialog.get_message(buf)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())