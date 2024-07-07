# Python - Classes and Objects

This directory contains solutions to various tasks related to defining and working with classes and objects in Python. The tasks focus on creating and managing squares, along with a task on singly linked lists. Each task is implemented in a Python script, and the specific tasks and their descriptions are provided below.

## Tasks

### 0. My first square
File: 0-square.py

Write an empty class `Square` that defines a square.

### 1. Square with size
File: 1-square.py

Write a class `Square` that defines a square by:
- Private instance attribute: `size`.
- Instantiation with `size` (no type/value verification).

### 2. Size validation
File: 2-square.py

Write a class `Square` that defines a square by:
- Private instance attribute: `size`.
- Instantiation with optional `size`: `def __init__(self, size=0)`.
  - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
  - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.

### 3. Area of a square
File: 3-square.py

Write a class `Square` that defines a square by:
- Private instance attribute: `size`.
- Instantiation with optional `size`: `def __init__(self, size=0)`.
  - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
  - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- Public instance method: `def area(self):` that returns the current square area.

### 4. Access and update private attribute
File: 4-square.py

Write a class `Square` that defines a square by:
- Private instance attribute: `size`.
  - Property `def size(self):` to retrieve it.
  - Property setter `def size(self, value):` to set it.
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
    - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- Instantiation with optional `size`: `def __init__(self, size=0)`.
- Public instance method: `def area(self):` that returns the current square area.

### 5. Printing a square
File: 5-square.py

Write a class `Square` that defines a square by:
- Private instance attribute: `size`.
  - Property `def size(self):` to retrieve it.
  - Property setter `def size(self, value):` to set it.
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
    - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- Instantiation with optional `size`: `def __init__(self, size=0)`.
- Public instance method: `def area(self):` that returns the current square area.
- Public instance method: `def my_print(self):` that prints in `stdout` the square with the character `#`.
  - If `size` is equal to 0, print an empty line.

### 6. Coordinates of a square
File: 6-square.py

Write a class `Square` that defines a square by:
- Private instance attribute: `size`.
  - Property `def size(self):` to retrieve it.
  - Property setter `def size(self, value):` to set it.
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
    - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- Private instance attribute: `position`.
  - Property `def position(self):` to retrieve it.
  - Property setter `def position(self, value):` to set it.
    - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`.
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0))`.
- Public instance method: `def area(self):` that returns the current square area.
- Public instance method: `def my_print(self):` that prints in `stdout` the square with the character `#`.
  - If `size` is equal to 0, print an empty line.

### 7. Singly linked list
File: 100-singly_linked_list.py

Write a class `Node` that defines a node of a singly linked list by:
- Private instance attribute: `data`.
  - Property `def data(self):` to retrieve it.
  - Property setter `def data(self, value):` to set it.
    - `data` must be an integer, otherwise raise a `TypeError` exception with the message `data must be an integer`.
- Private instance attribute: `next_node`.
  - Property `def next_node(self):` to retrieve it.
  - Property setter `def next_node(self, value):` to set it.
    - `next_node` can be `None` or must be a `Node`, otherwise raise a `TypeError` exception with the message `next_node must be a Node object`.
- Instantiation with `data` and `next_node`: `def __init__(self, data, next_node=None)`.

Write a class `SinglyLinkedList` that defines a singly linked list by:
- Private instance attribute: `head` (no setter or getter).
- Simple instantiation: `def __init__(self)`.
- Should be printable.
  - Print the entire list in `stdout`, one node number per line.
- Public instance method: `def sorted_insert(self, value):` that inserts a new `Node` into the correct sorted position in the list (increasing order).

### 8. Print Square instance
File: 101-square.py

Write a class `Square` that defines a square by:
- Private instance attribute: `size`.
  - Property `def size(self):` to retrieve it.
  - Property setter `def size(self, value):` to set it.
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
    - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- Private instance attribute: `position`.
  - Property `def position(self):` to retrieve it.
  - Property setter `def position(self, value):` to set it.
    - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`.
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0))`.
- Public instance method: `def area(self):` that returns the current square area.
- Public instance method: `def my_print(self):` that prints in `stdout` the square with the character `#`.
  - If `size` is equal to 0, print an empty line.
- Printing a `Square` instance should have the same behavior as `my_print()`.

### 9. Compare 2 squares
File: 102-square.py

Write a class `Square` that defines a square by:
- Private instance attribute: `size`.
  - Property `def size(self):` to retrieve it.
  - Property setter `def size(self, value):` to set it.
    - `size` must be a number (float or integer), otherwise raise a `TypeError` exception with the message `size must be a number`.
    - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- Instantiation with `size`: `def __init__(self, size=0)`.
- Public instance method: `def area(self):` that returns the current square area.
- `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<`, and `<=` based on the square area.

### 10. ByteCode -> Python #5
File: 103-magic_class.py

Write the Python class `MagicClass` that does exactly the same as the following Python bytecode:
