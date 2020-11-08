import Main as be
import XMLOut
import os
from shutil import copyfile
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt

class MainRunnerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    result = QtCore.pyqtSignal(object)

class MainRunner(QtCore.QRunnable):
    def __init__(self, inputs):
        super(MainRunner, self).__init__()
        self.inputs = inputs
        self.signals = MainRunnerSignals()

    @QtCore.pyqtSlot()
    def run(self):
        result = be.main(self.inputs)
        self.signals.result.emit(result)
        self.signals.finished.emit()

class MinorityGameGUI(XMLOut.Ui_Main):
    def __init__(self):
        super(MinorityGameGUI, self).__init__()

        self.threadpool = QtCore.QThreadPool()
        self.inputs = {
            #Disease inputs
            'startSickChance': 0.02,
            'startSymptomaticChance': 0.5,
            'rateOfSpread': 0.5,
            'sickTime': 1,
            'incubationTime': 14,
            'immuneTime': 10,
            
            #Groups inputs
            'numGroups': 200,
            'numAgents': 1000,
            'numRestaurants': 10,
            'gChance': 0.1,
            'aChance': 0.5,
            
            'numDays': 1000
        }

    def setupUi(self, Main):
        super(MinorityGameGUI, self).setupUi(Main)
        self.startButton.clicked.connect(self.startButtonClicked)
        self.loadButton.clicked.connect(self.loadButtonClicked)
        self.saveButton.clicked.connect(self.saveButtonClicked)

    def startButtonClicked(self):
        def setInputs():
            noError = True
            try:
                numAgents = numDays = incubationTime = numRestaurants = rateOfSpread = -1
                numAgents = int(self.popTextEdit.toPlainText())
                numDays = int(self.daysTextEdit.toPlainText())
                incubationTime = int(self.stimeTextEdit.toPlainText())
                numRestaurants = int(self.norTextEdit.toPlainText())
                rateOfSpread = float(self.rosTextEdit.toPlainText())
            except:
                noError = False
            finally:
                if numAgents >= 10 and numDays > 0 and incubationTime > 0 and numRestaurants > 0 and 0 <= rateOfSpread <= 1:
                    self.inputs['numAgents'] = numAgents
                    self.inputs['numGroups'] = numAgents // 5
                    self.inputs['numDays'] = numDays
                    self.inputs['incubationTime'] = incubationTime
                    self.inputs['numRestaurants'] = numRestaurants
                    self.inputs['rateOfSpread'] = rateOfSpread
                else:
                    noError = False
                return noError
        if setInputs(): #for full operation, use this line
            self.errorLabel.setText('Simulation Processing\nPlease Wait')
            self.startButton.setEnabled(False)
            self.loadButton.setEnabled(False)
            self.saveButton.setEnabled(False)
            mr = MainRunner(self.inputs)
            mr.signals.result.connect(self.startButtonResults)
            mr.signals.finished.connect(self.startButtonFinished)
            self.threadpool.start(mr)
        else:
            self.errorLabel.setText('One or Multiple\nInputs Invalid')

    def startButtonResults(self,outputs):
        sick, healthy, winners = outputs
        x = list(sick.keys())
        y = list((c,a,b) for a,b,c in zip(sick.values(),healthy.values(),winners.values()))
        plt.plot(x,y)
        plt.savefig('.\\__pictures__\\current.png')
        plt.close()
        self.outputLabel.setPixmap(QtGui.QPixmap('.\\__pictures__\\current.png'))

    def startButtonFinished(self):
        self.errorLabel.setText('No Errors\nCurrently Present')
        self.startButton.setEnabled(True)
        self.loadButton.setEnabled(True)
        self.saveButton.setEnabled(True)

    def loadButtonClicked(self):
        if not (os.path.exists(".\\__save__\\save.txt") and os.path.exists(".\\__save__\\save.png")):
            self.errorLabel.setText("No Save Data \nwas Found")
            return
        self.outputLabel.setPixmap(QtGui.QPixmap('.\\__save__\\save.png'))
        save = open(".\\__save__\\save.txt","r")
        saveData = save.read().split(',')
        save.close()
        self.popTextEdit.setText(saveData[0])
        self.daysTextEdit.setText(saveData[1])
        self.stimeTextEdit.setText(saveData[2])
        self.norTextEdit.setText(saveData[3])
        self.rosTextEdit.setText(saveData[4])
        self.startButton.setEnabled(True)
        self.loadButton.setEnabled(True)
        self.saveButton.setEnabled(True)
        self.errorLabel.setText('Data Loaded \nSucessfully')

    def saveButtonClicked(self):
        copyfile('.\\__pictures__\\current.png','.\\__save__\\save.png')
        if os.path.exists(".\\__save__\\save.txt"):
            os.remove(".\\__save__\\save.txt")
        saveData = ""
        saveData += str(self.inputs['numAgents']) + ','
        saveData += str(self.inputs['numDays']) + ','
        saveData += str(self.inputs['incubationTime']) + ','
        saveData += str(self.inputs['numRestaurants']) + ','
        saveData += str(self.inputs['rateOfSpread'])
        save = open(".\\__save__\\save.txt","w+")
        save.write(saveData)
        save.close()
        self.errorLabel.setText('Data Saved \nSuccessfully')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MinorityGameGUI()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())