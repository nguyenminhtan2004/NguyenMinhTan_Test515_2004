# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playfair.ui'
#
# Created for Câu 02 - PlayFair Cipher.
# Regenerate command:
# pyuic5 ui/playfair.ui -o ui/playfair.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 520)
        MainWindow.setWindowTitle("PlayFair Cipher")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.labelKey = QtWidgets.QLabel(self.centralwidget)
        self.labelKey.setObjectName("labelKey")
        self.gridLayout.addWidget(self.labelKey, 0, 0, 1, 1)

        self.txt_key = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_key.setObjectName("txt_key")
        self.gridLayout.addWidget(self.txt_key, 0, 1, 1, 1)

        self.labelInput = QtWidgets.QLabel(self.centralwidget)
        self.labelInput.setObjectName("labelInput")
        self.gridLayout.addWidget(self.labelInput, 1, 0, 1, 1)

        self.txt_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_input.setMinimumSize(QtCore.QSize(0, 100))
        self.txt_input.setObjectName("txt_input")
        self.gridLayout.addWidget(self.txt_input, 1, 1, 1, 1)

        self.labelOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelOutput.setObjectName("labelOutput")
        self.gridLayout.addWidget(self.labelOutput, 2, 0, 1, 1)

        self.txt_output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_output.setMinimumSize(QtCore.QSize(0, 100))
        self.txt_output.setReadOnly(True)
        self.txt_output.setObjectName("txt_output")
        self.gridLayout.addWidget(self.txt_output, 2, 1, 1, 1)

        self.labelMatrix = QtWidgets.QLabel(self.centralwidget)
        self.labelMatrix.setObjectName("labelMatrix")
        self.gridLayout.addWidget(self.labelMatrix, 3, 0, 1, 1)

        self.txt_matrix = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_matrix.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.txt_matrix.setFont(font)
        self.txt_matrix.setReadOnly(True)
        self.txt_matrix.setObjectName("txt_matrix")
        self.gridLayout.addWidget(self.txt_matrix, 3, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.horizontalLayout.addWidget(self.btn_encrypt)

        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.horizontalLayout.addWidget(self.btn_decrypt)

        self.btn_matrix = QtWidgets.QPushButton(self.centralwidget)
        self.btn_matrix.setObjectName("btn_matrix")
        self.horizontalLayout.addWidget(self.btn_matrix)

        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "PlayFair Cipher"))
        self.labelTitle.setText(_translate("MainWindow", "PLAYFAIR CIPHER"))
        self.labelKey.setText(_translate("MainWindow", "Key:"))
        self.txt_key.setText(_translate("MainWindow", "MONARCHY"))
        self.txt_key.setPlaceholderText(_translate("MainWindow", "Enter key"))
        self.labelInput.setText(_translate("MainWindow", "Input:"))
        self.txt_input.setPlainText(_translate("MainWindow", "INSTRUMENTS"))
        self.txt_input.setPlaceholderText(_translate("MainWindow", "Enter plaintext or ciphertext"))
        self.labelOutput.setText(_translate("MainWindow", "Output:"))
        self.txt_output.setPlaceholderText(_translate("MainWindow", "Result"))
        self.labelMatrix.setText(_translate("MainWindow", "Matrix:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_matrix.setText(_translate("MainWindow", "Generate Matrix"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
