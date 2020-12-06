# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setEnabled(True)
        Main.resize(540, 240)
        Main.setMinimumSize(QtCore.QSize(0, 0))
        Main.setMaximumSize(QtCore.QSize(1161, 806))
        Main.setBaseSize(QtCore.QSize(1161, 681))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.oldButton = QtWidgets.QPushButton(self.centralwidget)
        self.oldButton.setGeometry(QtCore.QRect(20, 100, 241, 51))
        self.oldButton.setObjectName("oldButton")
        self.finalTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.finalTextEdit.setGeometry(QtCore.QRect(20, 40, 241, 41))
        self.finalTextEdit.setPlaceholderText("")
        self.finalTextEdit.setObjectName("finalTextEdit")
        self.avgTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.avgTextEdit.setGeometry(QtCore.QRect(280, 40, 241, 41))
        self.avgTextEdit.setPlaceholderText("")
        self.avgTextEdit.setObjectName("avgTextEdit")
        self.finalLabel = QtWidgets.QLabel(self.centralwidget)
        self.finalLabel.setGeometry(QtCore.QRect(20, 10, 421, 21))
        self.finalLabel.setObjectName("finalLabel")
        self.avgLabel = QtWidgets.QLabel(self.centralwidget)
        self.avgLabel.setGeometry(QtCore.QRect(280, 10, 421, 21))
        self.avgLabel.setObjectName("avgLabel")
        self.midButton = QtWidgets.QPushButton(self.centralwidget)
        self.midButton.setEnabled(True)
        self.midButton.setGeometry(QtCore.QRect(280, 100, 241, 51))
        self.midButton.setObjectName("midButton")
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setEnabled(False)
        self.newButton.setGeometry(QtCore.QRect(20, 170, 241, 51))
        self.newButton.setObjectName("newButton")
        self.csvButton = QtWidgets.QPushButton(self.centralwidget)
        self.csvButton.setEnabled(True)
        self.csvButton.setGeometry(QtCore.QRect(280, 170, 241, 51))
        self.csvButton.setObjectName("csvButton")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Coronavirus Minority Game"))
        self.oldButton.setText(_translate("Main", "Load Oldest Save"))
        self.finalLabel.setText(_translate("Main", "Final Turnout:"))
        self.avgLabel.setText(_translate("Main", "Average Turnout:"))
        self.midButton.setText(_translate("Main", "Load Middle Save"))
        self.newButton.setText(_translate("Main", "Load Newest Save"))
        self.csvButton.setText(_translate("Main", "Convert To CSV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

