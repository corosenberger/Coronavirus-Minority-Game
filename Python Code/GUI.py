import Main as be
import GUI2 as av
import XMLOut
import os
import base64
from shutil import copyfile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
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
            'startSymptomaticChance': 1,
            'rateOfSpread': 1,
            'sickTime': 0,
            'incubationTime': 14,
            'immuneTime': 10,
            
            #Groups inputs
            'numGroups': 200,
            'numAgents': 1000,
            'numRestaurants': 10,
            'averageGroupSize': 5,
            
            'numDays': 1000,

            #Sub-team 2 Inputs
            'weather_condition': 5,
            'rate_of_spread': 1,
            'restaurant_capacity': 100,
            'un_employment_rate': 0,
            'num_agents': 10000,
            'num_rounds': 1000,

            'capacity': 100,
            'condition': 5,
            'urate': 0
        }
        self.window = QtWidgets.QMainWindow()
        self.ui = av.SettingsGUI(self.inputs)
        self.ui.setupUi(self.window)

    def setupUi(self, Main):
        super(MinorityGameGUI, self).setupUi(Main)
        self.startButton.clicked.connect(self.startButtonClicked)
        self.loadButton.clicked.connect(self.loadButtonClicked)
        self.saveButton.clicked.connect(self.saveButtonClicked)
        self.advancedButton.clicked.connect(self.advancedButtonClicked)

    def startButtonClicked(self):
        def setInputs():
            noError = True
            try:
                numAgents = int(self.popTextEdit.toPlainText())
                numDays = int(self.daysTextEdit.toPlainText())
                incubationTime = int(self.stimeTextEdit.toPlainText())
                numRestaurants = int(self.norTextEdit.toPlainText())
                rateOfSpread = float(self.rosTextEdit.toPlainText())
                weather = float(self.weatherTextEdit.toPlainText())
                capacity = int(self.capacityTextEdit.toPlainText())
                urate = float(self.urateTextEdit.toPlainText())
            except:
                noError = False
            finally:
                if noError and numAgents >= 10 and numDays > 0 and incubationTime > 0 and numRestaurants > 0 and \
                        0 <= rateOfSpread <= 3.5 and weather > 0 and capacity > 0 and 0 <= urate <= 1:
                    self.inputs['numAgents'] = self.inputs['num_agents']= numAgents
                    self.inputs['numGroups'] = numAgents // self.inputs['averageGroupSize']
                    self.inputs['numDays'] = self.inputs['num_rounds'] = numDays
                    self.inputs['incubationTime'] = incubationTime
                    self.inputs['numRestaurants'] = numRestaurants
                    self.inputs['rateOfSpread'] = rateOfSpread / incubationTime
                    self.inputs['rate_of_spread'] = rateOfSpread
                    self.inputs['condition'] = self.inputs['weather_condition'] = weather
                    self.inputs['capacity'] = self.inputs['restaurant_capacity'] = capacity
                    self.inputs['urate'] = self.inputs['un_employment_rate'] = urate
                else:
                    noError = False
                return noError
        if setInputs(): #for full operation, use this line
            self.errorLabel.setText('Simulation Processing\nPlease Wait')
            self.window.close()
            self.startButton.setEnabled(False)
            self.loadButton.setEnabled(False)
            self.saveButton.setEnabled(False)
            self.advancedButton.setEnabled(False)
            mr = MainRunner(self.inputs)
            mr.signals.result.connect(self.startButtonResults)
            mr.signals.finished.connect(self.startButtonFinished)
            self.threadpool.start(mr)
        else:
            self.errorLabel.setText('One or Multiple\nInputs Invalid')

    def startButtonResults(self,outputs):
        sick, healthy, attendance = outputs
        x = list(sick.keys())
        fig1 = plt.plot(x,sick.values(),label='Sick')
        fig2 = plt.plot(x,healthy.values(),label='Healthy')
        fig3 = plt.plot(x,attendance.values(),label='Attendance')
        plt.legend(handles=[fig1[0],fig2[0],fig3[0]])
        plt.savefig('.\\__pictures__\\current.png')
        plt.close()
        self.outputLabel.setPixmap(QtGui.QPixmap('.\\__pictures__\\current.png'))

    def startButtonFinished(self):
        self.errorLabel.setText('No Errors\nCurrently Present')
        self.startButton.setEnabled(True)
        self.loadButton.setEnabled(True)
        self.saveButton.setEnabled(True)
        self.advancedButton.setEnabled(True)

    def loadButtonClicked(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(filter='*.cmgsav')[0]

        if fname == '': return

        save = open(fname,'r')
        saveData = save.read()
        saveVals = saveData[:saveData.find('\n')].split(',')
        savePic = base64.b64decode(bytes(saveData[saveData.find('\n')+1:],'utf-8'))
        save.close()

        self.popTextEdit.setText(saveVals[0])
        self.inputs['numAgents'] = int(saveVals[0])
        self.daysTextEdit.setText(saveVals[1])
        self.inputs['numDays'] = int(saveVals[1])
        self.stimeTextEdit.setText(saveVals[2])
        self.inputs['incubationTime'] = int(saveVals[2])
        self.norTextEdit.setText(saveVals[3])
        self.inputs['numRestaurants'] = int(saveVals[3])
        self.rosTextEdit.setText(saveVals[4])
        self.inputs['rateOfSpread'] = float(saveVals[4]) / self.inputs['incubationTime']
        self.weatherTextEdit.setText(saveVals[5])
        self.inputs['condition'] = float(saveVals[5])
        self.capacityTextEdit.setText(saveVals[6])
        self.inputs['capacity'] = int(saveVals[6])
        self.urateTextEdit.setText(saveVals[7])
        self.inputs['urate'] = float(saveVals[7])
        self.inputs['startSickChance'] = float(saveVals[8])
        self.inputs['immuneTime'] = int(saveVals[9])
        self.inputs['averageGroupSize'] = int(saveVals[10])

        with open('.\\__pictures__\\current.png','wb') as currPic:
            currPic.truncate()
            currPic.write(savePic)
        self.outputLabel.setPixmap(QtGui.QPixmap('.\\__pictures__\\current.png'))

        self.startButton.setEnabled(True)
        self.loadButton.setEnabled(True)
        self.saveButton.setEnabled(True)
        self.advancedButton.setEnabled(True)
        self.errorLabel.setText('Data Loaded \nSucessfully')

    def saveButtonClicked(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(filter='*.cmgsav')[0]

        if fname == '': return

        saveData = ""
        saveData += str(self.inputs['numAgents']) + ','
        saveData += str(self.inputs['numDays']) + ','
        saveData += str(self.inputs['incubationTime']) + ','
        saveData += str(self.inputs['numRestaurants']) + ','
        saveData += str(self.inputs['rateOfSpread'] * self.inputs['incubationTime']) + ','
        saveData += str(self.inputs['condition']) + ','
        saveData += str(self.inputs['capacity']) + ','
        saveData += str(self.inputs['urate']) + ','
        saveData += str(self.inputs['startSickChance']) + ','
        saveData += str(self.inputs['immuneTime']) + ','
        saveData += str(self.inputs['averageGroupSize'])
        saveData += '\n'

        with open('.\\__pictures__\\current.png','rb') as savePic:
            picData = base64.b64encode(savePic.read())

        save = open(fname,'w+')
        save.write(saveData)
        save.close()
        save = open(fname,'ab')
        save.write(picData)
        save.close()

        self.errorLabel.setText('Data Saved \nSuccessfully')

    def advancedButtonClicked(self):
        self.ui.sschanceTextEdit.setText(str(self.inputs['startSickChance']))
        self.ui.imtimeTextEdit.setText(str(self.inputs['immuneTime']))
        self.ui.agsTextEdit.setText(str(self.inputs['averageGroupSize']))
        self.ui.errorLabel.setText('No Errors\nCurrently Present')
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MinorityGameGUI()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())