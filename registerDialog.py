# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Ui Files/registerdialog.ui'
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

class Ui_registerDialog(object):
    def setupUi(self, registerDialog):
        registerDialog.setObjectName(_fromUtf8("registerDialog"))
        registerDialog.resize(507, 199)
        self.label = QtGui.QLabel(registerDialog)
        self.label.setGeometry(QtCore.QRect(170, 33, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.reg_usernameBox = QtGui.QLineEdit(registerDialog)
        self.reg_usernameBox.setGeometry(QtCore.QRect(290, 30, 171, 27))
        self.reg_usernameBox.setObjectName(_fromUtf8("reg_usernameBox"))
        self.label_2 = QtGui.QLabel(registerDialog)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.reg_passwordBox = QtGui.QLineEdit(registerDialog)
        self.reg_passwordBox.setGeometry(QtCore.QRect(290, 70, 171, 27))
        self.reg_passwordBox.setText(_fromUtf8(""))
        self.reg_passwordBox.setEchoMode(QtGui.QLineEdit.Password)
        self.reg_passwordBox.setObjectName(_fromUtf8("reg_passwordBox"))
        self.reg_submit = QtGui.QPushButton(registerDialog)
        self.reg_submit.setGeometry(QtCore.QRect(170, 140, 141, 27))
        self.reg_submit.setObjectName(_fromUtf8("reg_submit"))
        self.reg_exit = QtGui.QPushButton(registerDialog)
        self.reg_exit.setGeometry(QtCore.QRect(318, 140, 141, 27))
        self.reg_exit.setObjectName(_fromUtf8("reg_exit"))
        self.label_3 = QtGui.QLabel(registerDialog)
        self.label_3.setGeometry(QtCore.QRect(60, 30, 71, 81))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("./Statics/add-user.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(registerDialog)
        QtCore.QMetaObject.connectSlotsByName(registerDialog)

    def retranslateUi(self, registerDialog):
        registerDialog.setWindowTitle(_translate("registerDialog", "Kayıt Ol", None))
        self.label.setText(_translate("registerDialog", "Kullanıcı Adı", None))
        self.label_2.setText(_translate("registerDialog", "Parola", None))
        self.reg_submit.setText(_translate("registerDialog", "Gönder", None))
        self.reg_exit.setText(_translate("registerDialog", "İptal", None))

