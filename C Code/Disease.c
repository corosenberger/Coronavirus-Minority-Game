#include "Disease.h"

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

PyMODINIT_FUNC PyInit_DiseaseC(void) {
    return PyModule_Create(&DiseaseC);
}