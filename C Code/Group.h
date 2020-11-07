#ifndef _GROUP_H
#define _GROUP_H

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <time.h>

static PyObject* processSubTeam2Input(PyObject* self, PyObject* args);
static PyObject* getGroupSizes(PyObject* self, PyObject* args);
static PyObject* getAttendees(PyObject* self, PyObject* args);
static PyObject* getWinners(PyObject* self, PyObject* args);
PyMODINIT_FUNC PyInit_GroupC(void);

static PyMethodDef GroupCMethods[] = {
    {"processSubTeam2Input", processSubTeam2Input, METH_VARARGS, NULL},
    {"getGroupSizes", getGroupSizes, METH_VARARGS, NULL},
    {"getAttendees", getAttendees, METH_VARARGS, NULL},
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

#define ASYMPTOMATIC 2
#define SYMPTOMATIC 3

#endif