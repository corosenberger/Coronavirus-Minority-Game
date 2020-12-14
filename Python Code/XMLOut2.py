# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setEnabled(True)
        Main.resize(531, 241)
        Main.setMinimumSize(QtCore.QSize(0, 0))
        Main.setMaximumSize(QtCore.QSize(1161, 806))
        Main.setBaseSize(QtCore.QSize(1161, 681))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(30, 180, 211, 51))
        self.applyButton.setObjectName("applyButton")
        self.sschanceTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.sschanceTextEdit.setGeometry(QtCore.QRect(20, 40, 241, 41))
        self.sschanceTextEdit.setObjectName("sschanceTextEdit")
        self.imtimeTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.imtimeTextEdit.setGeometry(QtCore.QRect(280, 40, 241, 41))
        self.imtimeTextEdit.setObjectName("imtimeTextEdit")
        self.agsTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.agsTextEdit.setGeometry(QtCore.QRect(20, 120, 241, 41))
        self.agsTextEdit.setObjectName("agsTextEdit")
        self.sschanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.sschanceLabel.setGeometry(QtCore.QRect(20, 10, 421, 21))
        self.sschanceLabel.setObjectName("sschanceLabel")
        self.imtimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.imtimeLabel.setGeometry(QtCore.QRect(280, 10, 421, 21))
        self.imtimeLabel.setObjectName("imtimeLabel")
        self.agsLabel = QtWidgets.QLabel(self.centralwidget)
        self.agsLabel.setGeometry(QtCore.QRect(20, 90, 421, 21))
        self.agsLabel.setObjectName("agsLabel")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setEnabled(True)
        self.closeButton.setGeometry(QtCore.QRect(290, 180, 211, 51))
        self.closeButton.setObjectName("closeButton")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(290, 90, 211, 71))
        self.errorLabel.setObjectName("errorLabel")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Coronavirus Minority Game"))
        self.applyButton.setText(_translate("Main", "Apply"))
        self.sschanceTextEdit.setPlaceholderText(_translate("Main", "Number between 0-1"))
        self.imtimeTextEdit.setPlaceholderText(_translate("Main", "Any Integer Greater than -2"))
        self.agsTextEdit.setPlaceholderText(_translate("Main", "Integer between 1-10"))
        self.sschanceLabel.setText(_translate("Main", "Start Sick Chance:"))
        self.imtimeLabel.setText(_translate("Main", "Immune Time"))
        self.agsLabel.setText(_translate("Main", "Average Group Size:"))
        self.closeButton.setText(_translate("Main", "Close"))
        self.errorLabel.setText(_translate("Main", "No Errors\n"
"Currently Present"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

