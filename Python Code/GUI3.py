import XMLOut3
import database as db
from PyQt5 import QtCore, QtGui, QtWidgets

class DatabaseGUI(XMLOut3.Ui_Main):
    def __init__(self):
        super(DatabaseGUI, self).__init__()
        self.final = self.avg = self.param = None

    def setupUi(self, Main):
        super(DatabaseGUI, self).setupUi(Main)
        self.oldButton.clicked.connect(self.oldButtonClicked)
        self.midButton.clicked.connect(self.midButtonClicked)
        self.newButton.clicked.connect(self.newButtonClicked)
        self.csvButton.clicked.connect(self.csvButtonClicked)
        self.finalTextEdit.setReadOnly(True)
        self.avgTextEdit.setReadOnly(True)

    def accessDatabase(self, index):
        database = db.database.load_save(index)
        self.final = database.final_turnout
        self.avg = database.turnout_per_round
        self.param = database.parameter_values

    def oldButtonClicked(self):
        self.accessDatabase(1)
        self.finalTextEdit.setText(str(self.final))
        self.avgTextEdit.setText(str(self.avg))
        self.oldButton.setEnabled(False)
        self.midButton.setEnabled(True)
        self.newButton.setEnabled(True)

    def midButtonClicked(self):
        self.accessDatabase(2)
        self.finalTextEdit.setText(str(self.final))
        self.avgTextEdit.setText(str(self.avg))
        self.oldButton.setEnabled(True)
        self.midButton.setEnabled(False)
        self.newButton.setEnabled(True)

    def newButtonClicked(self):
        self.accessDatabase(3)
        self.finalTextEdit.setText(str(self.final))
        self.avgTextEdit.setText(str(self.avg))
        self.oldButton.setEnabled(True)
        self.midButton.setEnabled(True)
        self.newButton.setEnabled(False)

    def csvButtonClicked(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(filter='*.csv')[0]
        if fname == '': return

        saveData = []
        for i in range(len(self.param[0])):
            d = i+1
            s = self.param[0][i]
            h = self.param[1][i]
            a = self.param[2][i]
            saveData.append([d,s,h,a])

        with open(fname,'w+') as save:
            save.write('Round Number,Sick,Healthy,Attendance\n')
            for d,s,h,a in saveData:
                save.write(str(d)+','+str(s)+','+str(h)+','+str(a)+'\n')