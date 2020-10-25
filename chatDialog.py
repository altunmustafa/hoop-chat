# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui Files/chatdialog.ui'
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

class Ui_chatDialog(object):
    def setupUi(self, chatDialog):
        chatDialog.setObjectName(_fromUtf8("chatDialog"))
        chatDialog.resize(462, 517)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chatDialog.sizePolicy().hasHeightForWidth())
        chatDialog.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(chatDialog)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chattingFriend = QtGui.QLabel(self.centralwidget)
        self.chattingFriend.setObjectName(_fromUtf8("chattingFriend"))
        self.gridLayout.addWidget(self.chattingFriend, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        chatDialog.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(chatDialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        chatDialog.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(chatDialog)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        chatDialog.setStatusBar(self.statusbar)

        self.retranslateUi(chatDialog)
        QtCore.QMetaObject.connectSlotsByName(chatDialog)

    def retranslateUi(self, chatDialog):
        chatDialog.setWindowTitle(_translate("chatDialog", "Sohbet", None))
        self.chattingFriend.setText(_translate("chatDialog", "TextLabel", None))

