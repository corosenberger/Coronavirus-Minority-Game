#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <time.h>

static PyObject* getGroupSizes(PyObject* self, PyObject* args) {
    srand(time(0));
    int numAgents;
    int numGroups;
    int maxSize;

    if (!PyArg_ParseTuple(args,"iii",&numAgents,&numGroups,&maxSize)) return NULL;

    int sizes[numGroups];
    PyObject* out = PyList_New(numGroups);

    for(int i = 0; i < numGroups; i++) sizes[i] = 1;

    int numLoops = numAgents-numGroups;
    for(int i = 0; i < numLoops; i++) {
        int randIdx = rand()%numGroups;
        sizes[randIdx]++;
        if(sizes[randIdx] == maxSize) {
            int temp = sizes[randIdx];
            sizes[randIdx] = sizes[numGroups-1];
            sizes[numGroups-1] = temp;
            numGroups--;
        }
    }

    for(int i = 0; i < PyList_Size(out); i++) PyList_SetItem(out,i,Py_BuildValue("i",sizes[i]));
    return out;
}

static PyObject* getWinners(PyObject* self, PyObject* args) {
    PyObject* agents;
    PyObject* sickness;

    if (!PyArg_ParseTuple(args,"OO",&agents,&sickness)) return NULL;
    if(!PyList_Check(agents)) return NULL;
    if(!PyList_Check(sickness)) return NULL;

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
        PyObject* awgo = PyObject_GetAttrString(agent,"willGoOut");
        int isSick = PyObject_IsTrue(PyList_GetItem(sickness,i));

        PyObject* wonRound;
        if(PyObject_IsTrue(awgo)) wonRound = (attendeesWin && !isSick) ? Py_True:Py_False;
        else wonRound = (homiesWin || isSick) ? Py_True:Py_False;

        PyObject_SetAttrString(agent,"wonLastRound",wonRound);
        PyList_SetItem(winners,i,wonRound);
    }

    return winners;
}

static PyMethodDef GroupCMethods[] = {
    {"getGroupSizes", getGroupSizes, METH_VARARGS, NULL},
    {"getWinners", getWinners, METH_VARARGS, NULL},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef GroupC = {
    PyModuleDef_HEAD_INIT,
    "GroupC",
    NULL,
    -1,
    GroupCMethods
};

PyMODINIT_FUNC PyInit_GroupC(void) {
    return PyModule_Create(&GroupC);
}