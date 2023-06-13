#include <Python.h>
void print_python_list_info(PyObject *p);

/**
*print_python_list_info - prints basic info about lists
*@p: pointer to the python object
*
*Return: this is a void function
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;
	const char *typeName;
	Py_ssize_t list_length;

	list_length = PyList_Size(list);
	printf("[*] Size of the Python List = %ld\n", list_length);
	printf("[*] Allocated = %ld\n", ((PyListObject *)list)->allocated);
	for (i = 0; i < list_length; i++)
	{
		PyObject *item = PyList_GetItem(list, i);

		typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}
