# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MangaProgressBar.ui'
#
# Created: Tue Feb 14 12:18:16 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MangaProgressBar(object):
    def setupUi(self, MangaProgressBar):
        MangaProgressBar.setObjectName(_fromUtf8("MangaProgressBar"))
        MangaProgressBar.resize(435, 110)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MangaProgressBar.sizePolicy().hasHeightForWidth())
        MangaProgressBar.setSizePolicy(sizePolicy)
        MangaProgressBar.setMinimumSize(QtCore.QSize(435, 110))
        MangaProgressBar.setMaximumSize(QtCore.QSize(435, 110))
        MangaProgressBar.setWindowTitle(_fromUtf8("MangaProgressBar"))
        MangaProgressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar = QtGui.QProgressBar(MangaProgressBar)
        self.progressBar.setGeometry(QtCore.QRect(10, 51, 421, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.btnOK = QtGui.QPushButton(MangaProgressBar)
        self.btnOK.setGeometry(QtCore.QRect(270, 81, 75, 23))
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.label = QtGui.QLabel(MangaProgressBar)
        self.label.setGeometry(QtCore.QRect(10, 81, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(MangaProgressBar)
        self.label_2.setGeometry(QtCore.QRect(180, 81, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QSpinBox(MangaProgressBar)
        self.spinBox.setGeometry(QtCore.QRect(140, 77, 35, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setProperty("value", 5)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.btnExit = QtGui.QPushButton(MangaProgressBar)
        self.btnExit.setGeometry(QtCore.QRect(350, 81, 75, 23))
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.groupBox = QtGui.QGroupBox(MangaProgressBar)
        self.groupBox.setGeometry(QtCore.QRect(5, 5, 425, 41))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btnSelectFile = QtGui.QPushButton(self.groupBox)
        self.btnSelectFile.setGeometry(QtCore.QRect(320, 14, 50, 23))
        self.btnSelectFile.setObjectName(_fromUtf8("btnSelectFile"))
        self.btnSelectFolder = QtGui.QPushButton(self.groupBox)
        self.btnSelectFolder.setGeometry(QtCore.QRect(370, 14, 50, 23))
        self.btnSelectFolder.setObjectName(_fromUtf8("btnSelectFolder"))
        self.lineFolder = QtGui.QLineEdit(self.groupBox)
        self.lineFolder.setGeometry(QtCore.QRect(5, 15, 312, 20))
        self.lineFolder.setObjectName(_fromUtf8("lineFolder"))

        self.retranslateUi(MangaProgressBar)
        QtCore.QMetaObject.connectSlotsByName(MangaProgressBar)
        MangaProgressBar.setTabOrder(self.lineFolder, self.btnSelectFile)
        MangaProgressBar.setTabOrder(self.btnSelectFile, self.btnSelectFolder)
        MangaProgressBar.setTabOrder(self.btnSelectFolder, self.spinBox)
        MangaProgressBar.setTabOrder(self.spinBox, self.btnOK)
        MangaProgressBar.setTabOrder(self.btnOK, self.btnExit)

    def retranslateUi(self, MangaProgressBar):
        self.btnOK.setText(QtGui.QApplication.translate("MangaProgressBar", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MangaProgressBar", "Размещать на каждой", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MangaProgressBar", "-й странице", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("MangaProgressBar", "Выход", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MangaProgressBar", "Исходная папка или файл", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectFile.setText(QtGui.QApplication.translate("MangaProgressBar", "Файл", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectFolder.setText(QtGui.QApplication.translate("MangaProgressBar", "Папка", None, QtGui.QApplication.UnicodeUTF8))
        self.lineFolder.setText(QtGui.QApplication.translate("MangaProgressBar", "C:\\TEMP\\Manga", None, QtGui.QApplication.UnicodeUTF8))

