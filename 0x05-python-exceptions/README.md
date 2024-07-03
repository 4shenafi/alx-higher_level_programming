# Python Exceptions

This directory contains solutions to various tasks related to handling exceptions in Python. The tasks are designed to help me learn how to use `try` and `except` blocks effectively, ensuring my programs can handle errors gracefully. Each task is implemented in a Python script, and I can find the specific tasks and their descriptions below.

## Tasks

### 0. Safe List Printing
**File:** `0-safe_print_list.py`

Write a function `safe_print_list(my_list=[], x=0)` that prints `x` elements of a list. The function handles cases where `x` exceeds the length of `my_list` and uses `try`/`except` to manage potential errors. The function returns the real number of elements printed.

### 1. Safe Printing of an Integers List
**File:** `1-safe_print_integer.py`

Write a function `safe_print_integer(value)` that prints an integer using `"{:d}".format()`. The function returns `True` if the value is an integer and was printed correctly, otherwise it returns `False`.

### 2. Print and Count Integers
**File:** `2-safe_print_list_integers.py`

Write a function `safe_print_list_integers(my_list=[], x=0)` that prints the first `x` elements of a list, but only if they are integers. Non-integer elements are skipped. The function returns the real number of integers printed.

### 3. Integers Division with Debug
**File:** `3-safe_print_division.py`

Write a function `safe_print_division(a, b)` that divides two integers and prints the result. The result is printed in the `finally` block, preceded by the message `Inside result:`. The function returns the result of the division, or `None` if an error occurred.

### 4. Divide a List
**File:** `4-list_division.py`

Write a function `list_division(my_list_1, my_list_2, list_length)` that divides elements of two lists element-wise. If an element cannot be divided, the function prints an error message and assigns a result of `0` for that division. The function returns a new list with the results of the divisions.

### 5. Raise Exception
**File:** `5-raise_exception.py`

Write a function `raise_exception()` that raises a `TypeError` exception. This is a simple demonstration of raising exceptions in Python.

### 6. Raise a Message
**File:** `6-raise_exception_msg.py`

Write a function `raise_exception_msg(message="")` that raises a `NameError` exception with a specified message. This task shows how to raise exceptions with custom messages.

### 7. Safe Integer Print with Error Message
**File:** `100-safe_print_integer_err.py`

Write a function `safe_print_integer_err(value)` that prints an integer. If the value is not an integer, the function prints an error message to `stderr` and returns `False`. Otherwise, it returns `True`.

### 8. Safe Function Execution
**File:** `101-safe_function.py`

Write a function `safe_function(fct, *args)` that executes a function safely. If an error occurs during the function execution, it prints an error message to `stderr` and returns `None`.

### 9. ByteCode -> Python #4
**File:** `102-magic_calculation.py`

Write a function `magic_calculation(a, b)` that emulates a given bytecode. This task involves understanding and converting Python bytecode to Python code.

### 10. CPython #2: PyFloatObject
**File:** `103-python.c`

Create three C functions that print basic info about Python lists, bytes, and float objects. These functions demonstrate how to interact with Python objects in C.

---

Each task is accompanied by a `main.py` file to test the implementation. Make sure to run the tests to verify the correctness of my solutions.