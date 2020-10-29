import Main as be
import XMLOut
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
            'startSickChance': 0.01,
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

    def startButtonClicked(self):
        def setInputs():
            noError = True
            try:
                numAgents = int(self.popTextEdit.toPlainText())
                numDays = int(self.daysTextEdit.toPlainText())
                incubationTime = int(self.stimeTextEdit.toPlainText())
                numRestaurants = int(self.norTextEdit.toPlainText())
                rateOfSpread = float(self.rosTextEdit.toPlainText())
            except:
                noError = False
            finally:
                if noError and numAgents >= 10 and numDays > 0 and incubationTime > 0 and numRestaurants > 0 and 0 <= rateOfSpread <= 1:
                    self.inputs['numAgents'] = numAgents
                    self.inputs['numGroups'] = numAgents // 5
                    self.inputs['numDays'] = numDays
                    self.inputs['incubationTime'] = incubationTime
                    self.inputs['numRestaurants'] = numRestaurants
                    self.inputs['rateOfSpread'] = rateOfSpread
                    return True
                else:
                    return False
        if setInputs():
            self.errorLabel.setText('Simulation Processing\nPlease Wait')
            self.startButton.setEnabled(False)
            mr = MainRunner(self.inputs)
            mr.signals.result.connect(self.startButtonResults)
            mr.signals.finished.connect(self.startButtonFinished)
            self.threadpool.start(mr)
        else:
            self.errorLabel.setText('One or Multiple\nInputs Invalid')

    def startButtonResults(self,outputs):
        sick, healthy, winners = outputs
        x = list(sick.keys())
        y = list((a,b,c) for a,b,c in zip(sick.values(),healthy.values(),winners.values()))
        plt.plot(x,y)
        plt.savefig('.\\__pictures__\\current.png')
        plt.close()
        self.outputLabel.setPixmap(QtGui.QPixmap('.\\__pictures__\\current.png'))

    def startButtonFinished(self):
        self.errorLabel.setText('No Errors\nCurrently Present')
        self.startButton.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MinorityGameGUI()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())