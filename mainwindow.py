# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui Files/mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(523, 464)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(523, 464))
        MainWindow.setMaximumSize(QtCore.QSize(523, 464))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(120, 200, 44, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(120, 160, 83, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.usernameBox = QtGui.QLineEdit(self.centralWidget)
        self.usernameBox.setGeometry(QtCore.QRect(230, 160, 161, 27))
        self.usernameBox.setObjectName(_fromUtf8("usernameBox"))
        self.passBox = QtGui.QLineEdit(self.centralWidget)
        self.passBox.setGeometry(QtCore.QRect(230, 200, 161, 27))
        self.passBox.setEchoMode(QtGui.QLineEdit.Password)
        self.passBox.setObjectName(_fromUtf8("passBox"))
        self.loginButton = QtGui.QPushButton(self.centralWidget)
        self.loginButton.setGeometry(QtCore.QRect(120, 260, 131, 27))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.exitButton = QtGui.QPushButton(self.centralWidget)
        self.exitButton.setGeometry(QtCore.QRect(270, 260, 121, 27))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(130, 310, 180, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.kayit_ol = QtGui.QLabel(self.centralWidget)
        self.kayit_ol.setGeometry(QtCore.QRect(320, 310, 55, 17))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.kayit_ol.setFont(font)
        self.kayit_ol.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kayit_ol.setObjectName(_fromUtf8("kayit_ol"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(90, 40, 351, 71))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("./Statics/hoop_logo.fw.png")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.usernameBox.raise_()
        self.passBox.raise_()
        self.loginButton.raise_()
        self.exitButton.raise_()
        self.label_2.raise_()
        self.kayit_ol.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 523, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuHoop = QtGui.QMenu(self.menuBar)
        self.menuHoop.setObjectName(_fromUtf8("menuHoop"))
        self.menuYard_m = QtGui.QMenu(self.menuBar)
        self.menuYard_m.setObjectName(_fromUtf8("menuYard_m"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionTeam = QtGui.QAction(MainWindow)
        self.actionTeam.setObjectName(_fromUtf8("actionTeam"))
        self.menuHoop.addAction(self.action_exit)
        self.menuYard_m.addAction(self.actionAbout)
        self.menuYard_m.addAction(self.actionTeam)
        self.menuBar.addAction(self.menuHoop.menuAction())
        self.menuBar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hoop Chat", None))
        self.label_3.setText(_translate("MainWindow", "Parola", None))
        self.label.setText(_translate("MainWindow", "Kullanıcı Adı", None))
        self.loginButton.setText(_translate("MainWindow", "Oturum Aç", None))
        self.exitButton.setText(_translate("MainWindow", "İptal", None))
        self.label_2.setText(_translate("MainWindow", "Henüz bir hesabın yok mu?", None))
        self.kayit_ol.setText(_translate("MainWindow", "Kayıt ol!", None))
        self.menuHoop.setTitle(_translate("MainWindow", "Hoop", None))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım", None))
        self.action_exit.setText(_translate("MainWindow", "Çıkış", None))
        self.actionAbout.setText(_translate("MainWindow", "Hoop Hakkında", None))
        self.actionTeam.setText(_translate("MainWindow", "Ekip", None))

