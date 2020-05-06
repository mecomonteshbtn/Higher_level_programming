#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - A function that prints information about a
 * python list object
 * @p: The pointer to generic PyObject which is of PyListObject type
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *py_list = NULL;
	size_t len = 0, i = 0;
	const char *py_type = NULL;

	len = PyList_Size(p);
	py_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	for  (; i < len; i++)
	{
		py_type = Py_TYPE(py_list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, py_type);
	}
}
