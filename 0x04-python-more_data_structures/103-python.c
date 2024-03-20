#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - prints info about Python bytes object
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *byte_obj = (PyBytesObject *)p;
    ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(byte_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        fflush(stdout);
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %ld bytes:", (size < 10) ? size : 10);
    for (i = 0; i < size && i < 10; ++i)
    {
        printf(" %02x", string[i] & 0xff);
    }
    printf("\n");
    fflush(stdout);
}

/**
 * print_python_list - prints info about Python list object
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
    PyListObject *list_obj = (PyListObject *)p;
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");

    if (!PyList_Check(list_obj))
    {
        printf("  [ERROR] Invalid List Object\n");
        fflush(stdout);
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list_obj->allocated);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: ", i);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyList_Check(item))
            print_python_list(item);
        else if (PyFloat_Check(item))
            printf("float\n");
        else if (PyTuple_Check(item))
            printf("tuple\n");
        else if (PyLong_Check(item))
            printf("int\n");
        else if (PyUnicode_Check(item))
            printf("str\n");
        else
            printf("%s\n", Py_TYPE(item)->tp_name);
    }
    fflush(stdout);
}

