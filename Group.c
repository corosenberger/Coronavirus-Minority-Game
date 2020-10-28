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

static PyMethodDef GroupCMethods[] = {
    {"getGroupSizes", getGroupSizes, METH_VARARGS, NULL},
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