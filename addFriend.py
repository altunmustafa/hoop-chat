# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui Files/addfriend.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_addFriend(object):
    def setupUi(self, addFriend):
        addFriend.setObjectName(_fromUtf8("addFriend"))
        addFriend.resize(503, 182)
        self.label = QtGui.QLabel(addFriend)
        self.label.setGeometry(QtCore.QRect(180, 42, 83, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(addFriend)
        self.label_2.setGeometry(QtCore.QRect(180, 75, 50, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.friend_uname = QtGui.QLineEdit(addFriend)
        self.friend_uname.setEnabled(True)
        self.friend_uname.setGeometry(QtCore.QRect(280, 37, 200, 27))
        self.friend_uname.setObjectName(_fromUtf8("friend_uname"))
        self.server = QtGui.QLineEdit(addFriend)
        self.server.setGeometry(QtCore.QRect(280, 70, 200, 27))
        self.server.setObjectName(_fromUtf8("server"))
        self.addFriendExit = QtGui.QPushButton(addFriend)
        self.addFriendExit.setGeometry(QtCore.QRect(390, 120, 91, 27))
        self.addFriendExit.setObjectName(_fromUtf8("addFriendExit"))
        self.addFriendSubmit = QtGui.QPushButton(addFriend)
        self.addFriendSubmit.setGeometry(QtCore.QRect(285, 120, 91, 27))
        self.addFriendSubmit.setObjectName(_fromUtf8("addFriendSubmit"))
        self.addFriendSymbol = QtGui.QLabel(addFriend)
        self.addFriendSymbol.setGeometry(QtCore.QRect(60, 30, 91, 81))
        self.addFriendSymbol.setText(_fromUtf8(""))
        self.addFriendSymbol.setPixmap(QtGui.QPixmap(_fromUtf8("./Statics/group.png")))
        self.addFriendSymbol.setObjectName(_fromUtf8("addFriendSymbol"))
        self.label_3 = QtGui.QLabel(addFriend)
        self.label_3.setGeometry(QtCore.QRect(60, 40, 71, 81))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("../Statics/group.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(addFriend)
        QtCore.QMetaObject.connectSlotsByName(addFriend)

    def retranslateUi(self, addFriend):
        addFriend.setWindowTitle(_translate("addFriend", "Arkadaş Ekle", None))
        self.label.setText(_translate("addFriend", "Kullanıcı Adı", None))
        self.label_2.setText(_translate("addFriend", "Sunucu", None))
        self.addFriendExit.setText(_translate("addFriend", "İptal", None))
        self.addFriendSubmit.setText(_translate("addFriend", "Ekle", None))

