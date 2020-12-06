import os
import pickle

# HOW TO USE DATABASE:
#       - add_save : To save a simulation, call the 'add_save' function and put in parameters...
#                * 'final_turnout': a parameter that takes in an (integer) representing the turnout of the final round
#                * 'turnout_per_round': a parameter that takes in an (array of integers) according to turnout per round
#                * 'parameter_values': a paramater that takes in an (array of integers) representing user input parameter values
#                       EXAMPLE OF CALL -> database.add_save(3, [4, 5, 9, 23], [24, 8, 5, 90])
#
#       - load_save : Returns a database object containing 'final_turnout', 'turnout_per_round', and 'parameter_values'
#                * Games are indexed 1-3, 1 being oldest save and 3 being newest
#                * When calling, 'save_number' should be an (integer) representing 1-3
#                * IMPORTANT!!! The properties of the object (like final_turnout) can be retrieved from the object by 
#                       EXAMPLE OF CALL (retrieving a database save object) -> database.load_save(2)
#                       EXAMPLE OF CALL (retrieving final_turnout of a save object) -> database.load_save(2).final_turnout
#
#       - erase_entire_file : Erases save file from computer
#                       EXAMPLE OF CALL -> database.erase_entire_file()
#
#       IMPORTANT: make sure to put in 'import database from database'


class database:

    # stores passed data in a database object (which will be stored in a database array, stored in data_file)
    def __init__(self, final_turnout, turnout_per_round, parameter_values):
        self.final_turnout = final_turnout
        self.turnout_per_round = turnout_per_round
        self.parameter_values = parameter_values

    # CALLABLE METHOD: to save a game simulation, appends the newly made 'game_save' in the 'game_save_array'
    @classmethod
    def add_save(cls, final_turnout, turnout_per_round, parameter_values): 
        save_array = []
        if os.path.exists('restaurant_game_data_file'): # checks to see if data file already exists on computer, loads old data
            erase = False
            with open('restaurant_game_data_file','rb') as rfp:
                save_array = pickle.load(rfp)
                erase = True
            if erase: database.erase_entire_file()
        temp_save = database(final_turnout, turnout_per_round, parameter_values)
        save_array.append(temp_save)
        database.store_save(save_array)

    # method for storing 'game_save_array' in 'data_file', checks size of array first to determine if stack needs to push first
    @classmethod
    def store_save(cls, save_array): 
        if len(save_array) > 3:
            del save_array[0]
        my_object = save_array
        with open('restaurant_game_data_file','wb') as wfp:
            pickle.dump(my_object, wfp)

    # CALLABLE METHOD: returns a database object containing 'final_turnout', 'turnout_per_round', and 'parameter_values'
    # games are indexed 1-3, 1 being oldest save and 3 being newest
    # when calling, 'save_number' should be an (integer) representing 1-3
    @classmethod
    def load_save(cls, save_number): 
        with open('restaurant_game_data_file','rb') as rfp:
            my_object = pickle.load(rfp)
            return my_object[save_number - 1]

    @classmethod
    # CALLABLE METHOD: erases data file completely from computer
    def erase_entire_file(cls):
        if os.path.exists("restaurant_game_data_file"):
            os.remove("restaurant_game_data_file")
        else:
            print("null")