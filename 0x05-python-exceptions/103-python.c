#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *item;

    if (!PyList_Check(p))
    {
        PyErr_Format(PyExc_TypeError, "Invalid List Object");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p))
    {
        PyErr_Format(PyExc_TypeError, "Invalid Bytes Object");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %d bytes: ", (int)(size > 10 ? 10 : size));
    for (i = 0; i < (size > 10 ? 10 : size); i++)
    {
        printf("%02x ", str[i] & 0xff);
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        PyErr_Format(PyExc_TypeError, "Invalid Float Object");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", PyFloat_AsDouble(p));
}

int main(void)
{
    // Example usage
    PyObject *list = PyList_New(0);
    PyObject *bytes = PyBytes_FromStringAndSize("Hello", 5);
    PyObject *flt = PyFloat_FromDouble(3.14);

    print_python_list(list);
    print_python_bytes(bytes);
    print_python_float(flt);

    Py_DECREF(list);
    Py_DECREF(bytes);
    Py_DECREF(flt);

    return 0;
}
