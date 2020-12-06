import XMLOut2
from PyQt5 import QtCore, QtGui, QtWidgets

class SettingsGUI(XMLOut2.Ui_Main):
    def __init__(self, inputs):
        super(SettingsGUI, self).__init__()
        self.inputs = inputs

    def setupUi(self, Main):
        super(SettingsGUI, self).setupUi(Main)
        self.applyButton.clicked.connect(self.applyButtonClicked)
        self.closeButton.clicked.connect(Main.close)

    def applyButtonClicked(self):
        def setInputs():
            noError = True
            try:
                sschance = float(self.sschanceTextEdit.toPlainText())
                imtime = int(self.imtimeTextEdit.toPlainText())
                ags = int(self.agsTextEdit.toPlainText())
            except:
                noError = False
            finally:
                if noError and 0 <= sschance <= 1 and imtime > 0 and 0 < ags <= 10:
                    self.inputs['startSickChance'] = sschance
                    self.inputs['immuneTime'] = imtime
                    self.inputs['averageGroupSize'] = ags
                else:
                    noError = False
                return noError
        if setInputs():
            self.errorLabel.setText('Inputs Applied \nSuccessfully')
        else:
            self.errorLabel.setText('One or Multiple\nInputs Invalid')
