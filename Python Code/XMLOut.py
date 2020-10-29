# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1161, 681)
        Main.setMinimumSize(QtCore.QSize(1161, 681))
        Main.setMaximumSize(QtCore.QSize(1161, 681))
        Main.setBaseSize(QtCore.QSize(1161, 681))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(280, 620, 281, 51))
        self.startButton.setObjectName("startButton")
        self.popTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.popTextEdit.setGeometry(QtCore.QRect(20, 40, 241, 41))
        self.popTextEdit.setObjectName("popTextEdit")
        self.daysTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.daysTextEdit.setGeometry(QtCore.QRect(20, 130, 241, 41))
        self.daysTextEdit.setObjectName("daysTextEdit")
        self.stimeTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.stimeTextEdit.setGeometry(QtCore.QRect(20, 220, 241, 41))
        self.stimeTextEdit.setObjectName("stimeTextEdit")
        self.norTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.norTextEdit.setGeometry(QtCore.QRect(20, 310, 241, 41))
        self.norTextEdit.setObjectName("norTextEdit")
        self.popLabel = QtWidgets.QLabel(self.centralwidget)
        self.popLabel.setGeometry(QtCore.QRect(20, 10, 421, 21))
        self.popLabel.setObjectName("popLabel")
        self.daysLabel = QtWidgets.QLabel(self.centralwidget)
        self.daysLabel.setGeometry(QtCore.QRect(20, 100, 421, 21))
        self.daysLabel.setObjectName("daysLabel")
        self.itimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.itimeLabel.setGeometry(QtCore.QRect(20, 190, 421, 21))
        self.itimeLabel.setObjectName("itimeLabel")
        self.norLabel = QtWidgets.QLabel(self.centralwidget)
        self.norLabel.setGeometry(QtCore.QRect(20, 280, 421, 21))
        self.norLabel.setObjectName("norLabel")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setEnabled(False)
        self.loadButton.setGeometry(QtCore.QRect(570, 620, 281, 51))
        self.loadButton.setObjectName("loadButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QtCore.QRect(860, 620, 281, 51))
        self.saveButton.setObjectName("saveButton")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(280, 10, 861, 601))
        self.outputLabel.setText("")
        self.outputLabel.setPixmap(QtGui.QPixmap(".\\__pictures__\\blank.png"))
        self.outputLabel.setScaledContents(True)
        self.outputLabel.setObjectName("outputLabel")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(40, 530, 211, 71))
        self.errorLabel.setObjectName("errorLabel")
        self.rosTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.rosTextEdit.setGeometry(QtCore.QRect(20, 410, 241, 41))
        self.rosTextEdit.setObjectName("rosTextEdit")
        self.rosLabel = QtWidgets.QLabel(self.centralwidget)
        self.rosLabel.setGeometry(QtCore.QRect(20, 380, 421, 21))
        self.rosLabel.setObjectName("rosLabel")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Coronavirus Minority Game"))
        self.startButton.setText(_translate("Main", "Start"))
        self.popLabel.setText(_translate("Main", "Population Size:"))
        self.daysLabel.setText(_translate("Main", "Number of Days:"))
        self.itimeLabel.setText(_translate("Main", "Sick Time:"))
        self.norLabel.setText(_translate("Main", "Number of Restaurants:"))
        self.loadButton.setText(_translate("Main", "Load"))
        self.saveButton.setText(_translate("Main", "Save"))
        self.errorLabel.setText(_translate("Main", "No Errors\n"
"Currently Present"))
        self.rosLabel.setText(_translate("Main", "Rate of Spread:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

