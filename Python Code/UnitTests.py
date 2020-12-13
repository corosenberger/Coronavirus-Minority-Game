import Main
import GUI
import Agent
import Group
import Disease
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def MainTest():
    inputs = {
        #Disease inputs
        'startSickChance': 0.02,
        'startSymptomaticChance': 0.5,
        'rateOfSpread': 1,
        'sickTime': 0,
        'incubationTime': 14,
        'immuneTime': 10,
            
        #Groups inputs
        'numGroups': 2,
        'numAgents': 10,
        'numRestaurants': 10,
        'averageGroupSize': 5,
            
        'numDays': 1,

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
    Main.main(inputs)

def GUITest():
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = GUI.MinorityGameGUI()
    ui.setupUi(Main)

def GroupTest():
    group = Group.Groups(10,100,10,Disease.Disease(0.1,0.1,1,1,1,1))
    group.passDay([1 for _ in group.agents])
    group.getAttendees()
    group.getHealthy()
    group.getWinners()
    group.getSick()

def DiseaseTest():
    disease = Disease.Disease(0.1,0.1,1,1,1,1)
    disease.infect([])

def AgentTest():
    agent = Agent.Agent(Disease.Disease(0.1,0.1,1,1,1,1))
    agent.passDay(Disease.Disease(0.1,0.1,1,1,1,1))

if __name__ == '__main__':
    MainTest()
    GUITest()
    GroupTest()
    DiseaseTest()
    AgentTest()
    