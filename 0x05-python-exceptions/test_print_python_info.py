import ctypes

# Load the shared library
lib = ctypes.CDLL('./libPython.so')

# Define the Python objects
my_list = [1, 2, 3]
my_bytes = b'Hello, World!'
my_float = 3.14

# Convert the Python objects to ctypes objects
py_list = ctypes.py_object(my_list)
py_bytes = ctypes.py_object(my_bytes)
py_float = ctypes.py_object(my_float)

# Call the C functions
lib.print_python_list(py_list)
lib.print_python_bytes(py_bytes)
lib.print_python_float(py_float)
