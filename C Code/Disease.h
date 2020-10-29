#ifndef _DISEASE_H
#define _DISEASE_H

#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* getChanceOfInfection(PyObject* self, PyObject* args);
PyMODINIT_FUNC PyInit_DiseaseC(void);

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

#endif