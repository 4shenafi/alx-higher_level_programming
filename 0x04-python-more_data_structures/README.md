# 0x04-python-more_data_structures

This directory contains various Python scripts focused on advanced data structures. Below is a description of each file and its associated functionality.

## Files and Descriptions

### 0-square_matrix_simple.py
**Task:** Write a function that computes the square value of all integers in a matrix.
- **Function:** `def square_matrix_simple(matrix=[])`
- **Description:** Returns a new matrix where each value is the square of the value of the input matrix. The initial matrix should not be modified.

### 1-search_replace.py
**Task:** Write a function that replaces all occurrences of an element by another in a new list.
- **Function:** `def search_replace(my_list, search, replace)`
- **Description:** Returns a new list where all occurrences of `search` in `my_list` are replaced by `replace`. The initial list should not be modified.

### 2-uniq_add.py
**Task:** Write a function that adds all unique integers in a list (only once for each integer).
- **Function:** `def uniq_add(my_list=[])`
- **Description:** Adds all unique integers in a list and returns their sum.

### 3-common_elements.py
**Task:** Write a function that returns a set of common elements in two sets.
- **Function:** `def common_elements(set_1, set_2)`
- **Description:** Returns a set containing elements common to both `set_1` and `set_2`.

### 4-only_diff_elements.py
**Task:** Write a function that returns a set of all elements present in only one set.
- **Function:** `def only_diff_elements(set_1, set_2)`
- **Description:** Returns a set containing elements that are only in one of the sets `set_1` or `set_2` but not both.

### 5-number_keys.py
**Task:** Write a function that returns the number of keys in a dictionary.
- **Function:** `def number_keys(a_dictionary)`
- **Description:** Returns the number of keys in the dictionary `a_dictionary`.

### 6-print_sorted_dictionary.py
**Task:** Write a function that prints a dictionary by ordered keys.
- **Function:** `def print_sorted_dictionary(a_dictionary)`
- **Description:** Prints the dictionary `a_dictionary` with its keys sorted in ascending order.

### 7-update_dictionary.py
**Task:** Write a function that replaces or adds key/value in a dictionary.
- **Function:** `def update_dictionary(a_dictionary, key, value)`
- **Description:** Updates or adds the key-value pair in `a_dictionary`.

### 8-simple_delete.py
**Task:** Write a function that deletes a key in a dictionary.
- **Function:** `def simple_delete(a_dictionary, key="")`
- **Description:** Deletes the key-value pair in `a_dictionary` for the specified key.

### 9-multiply_by_2.py
**Task:** Write a function that returns a new dictionary with all values multiplied by 2.
- **Function:** `def multiply_by_2(a_dictionary)`
- **Description:** Returns a new dictionary with each value in `a_dictionary` multiplied by 2.

### 10-best_score.py
**Task:** Write a function that returns a key with the biggest integer value.
- **Function:** `def best_score(a_dictionary)`
- **Description:** Returns the key with the highest integer value in `a_dictionary`.

### 11-multiply_list_map.py
**Task:** Write a function that returns a list with all values multiplied by a number without using any loops.
- **Function:** `def multiply_list_map(my_list=[], number=0)`
- **Description:** Returns a new list with each value in `my_list` multiplied by `number`.

### 12-roman_to_int.py
**Task:** Write a function that converts a Roman numeral to an integer.
- **Function:** `def roman_to_int(roman_string)`
- **Description:** Converts a Roman numeral string to an integer.

### 100-weight_average.py
**Task:** Write a function that returns the weighted average of all integers tuple (<score>, <weight>).
- **Function:** `def weight_average(my_list=[])`
- **Description:** Returns the weighted average of the scores in the list of tuples `my_list`.

### 101-square_matrix_map.py
**Task:** Write a function that computes the square value of all integers in a matrix using `map`.
- **Function:** `def square_matrix_map(matrix=[])`
- **Description:** Returns a new matrix where each value is the square of the value of the input matrix using `map`.

### 102-complex_delete.py
**Task:** Write a function that deletes keys with a specific value in a dictionary.
- **Function:** `def complex_delete(a_dictionary, value)`
- **Description:** Deletes keys in `a_dictionary` that have the specified value.

### 103-python.c
**Task:** Create two C functions that print some basic info about Python lists and Python bytes objects.
- **Functions:**
  - `void print_python_list(PyObject *p)`
  - `void print_python_bytes(PyObject *p)`
- **Description:** Prints information about Python lists and bytes objects.

---

This README provides a high-level overview of the tasks and functions implemented in each file within this directory.
