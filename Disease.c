#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* getChanceOfInfection(PyObject* self, PyObject* args) {
    double rate;
    int numInfected;

    if (!PyArg_ParseTuple(args,"di",&rate,&numInfected)) return NULL;

    double out = 1;
    double a = 1 - rate;
    unsigned long long n = numInfected;
    while (n) {
    	if (n & 1) out *= a;
    	a *= a;
    	n >>= 1;
    }
    out = 1-out;

    return Py_BuildValue("d", out);
}

static PyMethodDef DiseaseCMethods[] = {
    {"getChanceOfInfection", getChanceOfInfection, METH_VARARGS, NULL},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef DiseaseC = {
    PyModuleDef_HEAD_INIT,
    "DiseaseC",
    NULL,
    -1,
    DiseaseCMethods
};

PyMODINIT_FUNC PyInit_DiseaseC(void) {
    return PyModule_Create(&DiseaseC);
}