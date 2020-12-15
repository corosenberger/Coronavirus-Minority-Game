# Coronavirus-Minority-Game

## Files:

### C Code:

#### Disease.c, Disease.h:

Contains C functions used for calculating whether or not an agent gets infected

#### Group.c, Group.h:

Contains C functions used to speed up various calculations involving groups, such as determining the sizes of each group

### Python Code:

#### Agent.py:

Defines the properties of an agent of the minority game, such as whether they are currently infected and for how long

#### Brain.py:

Contains the source could for a multi-layered perceptron; used in the minority game to determine whether a group will go out

#### Disease.py:

Defines the properties for the current virus in the minority game

#### Group.py:

Defines the properties of the groups; contains methods used to calculate group decisions

#### GUI.py:

Contains the code defining the main GUI used in the minority game

#### GUI2.py:

Contains the code defining the advanced settings GUI used in the minority game

#### GUI3.py:

Contains the code defining the database GUI used in the minority game

#### Main.py:

Contains the main function used to run the back-end of the program

#### XMLOut.py, XMLOut2.py, XMLOut3.py:

Contains the raw code that was compiled from the .ui files

#### databases.py:

Defines the properties of the database use in the minority game

#### methods.py:

Contains methods used to calculate individual agent decisions

#### start.py:

Old main file, contains some extraneous code used in calculating individual agent decisions and database operations

## How to Compile:

If you are using windows, it should already be compiled for you.

If you are on Mac or Linux, complete the following steps:
-Open the makefile
-Download anaconda from the internet if you do not already have it
-Change DelCom to rm
-change PythonHeaderLocation to the location of your Python.h file
-change PythonFlagLibLocation to the location of the libraries associated with compiling python C code
-change PythonVersionFlag with your python version; e.i python version 3.8.* => -lpython38
-Change anything ending with .pyd to .so
-Compile (make all)

## How to Run:

Set your local directory to the outer directory (the one with the .ui files) and run the GUI.py file (that's it!)

## Authentication:

No authentication needed

## Allowed Values for Parameters:

### Population Size

Describes the number of agents in the minority game; can be any integer greater than 10

### Number of Days

Describes the number of rounds the minority game lasts for; can be any integer greater than 0

### Sick Time

Describes how many rounds an infected agent will be sick for; can be any integer greater than 0

### Number of Restaurants

Describes how many places the agents have to choose from; can be any number integer than 0

### Rate of Spread

Describes the r0 value associated with the virus; can be any number between 0 and 3.5

### Weather Condition

Describes a value describing how good or bad the weather is, 1 being very good weather and 5 being very bad weather; can be any number between 1 and 5

### Restaurant Capacity

Describes how many agents can go to each restaurant; can be any integer greater than 0

### Unemployment Rate

Describes the percentage of the population that currently does not have a job; can be any number between 0 and 1

### Start Sick Chance

Describes how likely an agent is to be infected at the start of the minority game; can be any number between 0 and 1

### Immune Time 

Describes how long an agent is immune to the virus after recovery; can be any integer greater than or equal to -1 (-1 being immune forever)

### Average Group Size 

Describes the average number of agents in each group; can be any integer between 1 and 10

### Final Demo Video
https://youtu.be/61AHO1mIoRo
