import Main
import GUI
import Agent
import Group
import Disease
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def test1():
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

def test2():
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
        'numAgents': 100,
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

def test3():
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = GUI.MinorityGameGUI()
    ui.setupUi(Main)
    ui.loadButtonClicked()
    ui.startButtonClicked()

if __name__ == '__main__':
    test1()
    test2()
    test3()