#include "Group.h"

static PyObject* processSubTeam2Input(PyObject* self, PyObject* args) {
    PyObject* groups;
    PyObject* subTeam2Input;

    if(!PyArg_ParseTuple(args,"OO",&groups,&subTeam2Input)) return NULL;

    int k = 0;
    for(int i = 0; i < PyList_Size(groups); i++) {
        PyObject* group = PyList_GetItem(groups,i);
        PyObject* agents = PyObject_GetAttrString(group,"agents");
        PyObject* brainInput = PyList_New(2*PyList_Size(agents));

        for(int j = 0; j < PyList_Size(agents); j++) {
            PyObject* agent = PyList_GetItem(agents,j);
            PyObject* wgo = PyList_GetItem(subTeam2Input,k++);
            PyObject* wlr = PyObject_GetAttrString(agent,"wonLastRound");

            PyObject_SetAttrString(agent,"willGoOut",wgo);
            PyList_SetItem(brainInput,j,wgo);
            PyList_SetItem(brainInput,PyList_Size(agents)+j,wlr);
        }

        PyObject_SetAttrString(group,"brainInput",brainInput);
    }

    return Py_None;
}

static PyObject* getGroupSizes(PyObject* self, PyObject* args) {
    srand(time(0));
    int numAgents;
    int numGroups;
    int maxSize;

    if(!PyArg_ParseTuple(args,"iii",&numAgents,&numGroups,&maxSize)) return NULL;

    int sizes[numGroups];
    PyObject* out = PyList_New(numGroups);

    for(int i = 0; i < numGroups; i++) sizes[i] = 1;

    int numLoops = numAgents-numGroups;
    for(int i = 0; i < numLoops; i++) {
        int randIdx = rand()%numGroups;
        sizes[randIdx]++;
        if(sizes[randIdx] == maxSize) {
            sizes[randIdx] ^= sizes[numGroups-1] ^= sizes[randIdx] ^= sizes[numGroups-1]; //swap
            numGroups--;
        }
    }

    for(int i = 0; i < PyList_Size(out); i++) PyList_SetItem(out,i,Py_BuildValue("i",sizes[i]));
    return out;
}

static PyObject* getAttendees(PyObject* self, PyObject* args) {
    PyObject* prefs;
    PyObject* outs;
    int numRestaurants;

    if(!PyArg_ParseTuple(args,"OOi",&prefs,&outs,&numRestaurants)) return NULL;

    PyObject* attendees = PyList_New(numRestaurants);
    for(int i = 0; i < PyList_Size(attendees); i++) PyList_SetItem(attendees,i,PyList_New(0));
    
    for(int i = 0; i < PyList_Size(prefs); i++) {
        long p = PyLong_AsLong(PyList_GetItem(prefs,i));
        PyObject* g = PyList_GetItem(outs,i);
        PyObject* res = PyList_GetItem(attendees,p);
        PyList_Append(res,g);
    }

    return attendees;
}

static PyObject* getWinners(PyObject* self, PyObject* args) {
    PyObject* agents;

    if(!PyArg_ParseTuple(args,"O",&agents)) return NULL;
    if(!PyList_Check(agents)) return NULL;

    int numAttendeesWeighted = 0;
    for(int i = 0; i < PyList_Size(agents); i++) {
        PyObject* agent = PyList_GetItem(agents,i);
        PyObject* awgo = PyObject_GetAttrString(agent,"willGoOut");
        if(PyObject_IsTrue(awgo)) numAttendeesWeighted++;
    }
    numAttendeesWeighted *= 2;

    PyObject* winners = PyList_New(PyList_Size(agents));
    int attendeesWin = numAttendeesWeighted <= PyList_Size(agents);
    int homiesWin = numAttendeesWeighted > PyList_Size(agents);
    for(int i = 0; i < PyList_Size(agents); i++) {
        PyObject* agent = PyList_GetItem(agents,i);
        PyObject* awgo = PyObject_GetAttrString(agent,"wentOut");
        long phase = PyLong_AsLong(PyObject_GetAttrString(agent,"phase"));
        int isSick = phase == ASYMPTOMATIC || phase == SYMPTOMATIC;

        PyObject* wonRound;
        if(PyObject_IsTrue(awgo)) wonRound = (attendeesWin && !isSick) ? Py_True:Py_False;
        else wonRound = (homiesWin || isSick) ? Py_True:Py_False;

        PyObject_SetAttrString(agent,"wonLastRound",wonRound);
        PyObject_SetAttrString(agent,"wentOut",Py_False);
        PyList_SetItem(winners,i,wonRound);
    }

    return winners;
}

PyMODINIT_FUNC PyInit_GroupC(void) {
    return PyModule_Create(&GroupC);
}