#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* getChanceOfInfection(PyObject* self, PyObject* args) {
    double rate;
    int numInfected;

    if (!PyArg_ParseTuple(args,"di",&rate,&numInfected))
        return NULL;

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

static PyMethodDef CExtensionMethods[] = {
    {"getChanceOfInfection", getChanceOfInfection, METH_VARARGS, NULL},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef CExtension = {
    PyModuleDef_HEAD_INIT,
    "CExtension",
    NULL,
    -1,
    CExtensionMethods
};

PyMODINIT_FUNC PyInit_CExtension(void) {
    return PyModule_Create(&CExtension);
}