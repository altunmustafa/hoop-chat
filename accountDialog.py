# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui Files/accountDialog.ui'
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

class Ui_accountDialog(object):
    def setupUi(self, accountDialog):
        accountDialog.setObjectName(_fromUtf8("accountDialog"))
        accountDialog.resize(279, 445)
        self.centralwidget = QtGui.QWidget(accountDialog)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        accountDialog.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(accountDialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 279, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHesap = QtGui.QMenu(self.menubar)
        self.menuHesap.setObjectName(_fromUtf8("menuHesap"))
        accountDialog.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(accountDialog)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        accountDialog.setStatusBar(self.statusbar)
        self.actionAdd_Friend = QtGui.QAction(accountDialog)
        self.actionAdd_Friend.setObjectName(_fromUtf8("actionAdd_Friend"))
        self.action_k = QtGui.QAction(accountDialog)
        self.action_k.setObjectName(_fromUtf8("action_k"))
        self.menuHesap.addAction(self.actionAdd_Friend)
        self.menubar.addAction(self.menuHesap.menuAction())

        self.retranslateUi(accountDialog)
        QtCore.QMetaObject.connectSlotsByName(accountDialog)

    def retranslateUi(self, accountDialog):
        accountDialog.setWindowTitle(_translate("accountDialog", "Arkadaş Listesi", None))
        self.menuHesap.setTitle(_translate("accountDialog", "Hesap", None))
        self.actionAdd_Friend.setText(_translate("accountDialog", "Arkadaş Ekle", None))
        self.action_k.setText(_translate("accountDialog", "Çıkış", None))

