 Python - Data Structures: Lists, Tuples

In this project, I learned about how sequence data types work in

# Resources

- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (until 5.3. Tuples and Sequences included)]
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)


In this project, I learned about how sequence data types work 
Python - specifically, lists and tuples.

## Tests :heavy_check_mark:
@@ -29,24 +37,40 @@ Prototypes for functions written in this project:

## Tasks :page_with_curl:

* **0. Print a list of integers**
  * [0-print_list_integer.py](./0-print_list_integer.py): Python function that prints all
  integers of a list, one per line.
  * Without importing modules or casting integers into strings.
## 0. Print a list of integers

Write a function that prints all integers of a list.

- Prototype: `def print_list_integer(my_list=[]):`
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers


## 1. Secure access to an element in a list

Write a function that retrieves an element from a list like in C.

- Prototype: `def element_at(my_list, idx):`
- If `idx` is negative, the function should return `None`
- If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
- You are not allowed to import any module
- You are not allowed to use `try/except`



## 2. Replace element

wite a function that replaces an element of a list at a specific position (like in C).

- Prototype: def replace_in_list(my_list, idx, element):
- If idx is negative, the function should not modify anything, and returns the original list
- If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use try/except

* **1. Secure access to an element in a list**
  * [1-element_at.py](./1-element_at.py): Python function that retrieves an element
  from a list.
  * If `idx` is negative or out of range (greater than the number of elements in
  `my_list`), the function returns `None`.
  * Without import modules or using `try/except`.

* **2. Replace element**
  * [2-replace_in_list.py](./2-replace_in_list.py): Python function that replaces an element
  of a list at a specific position.
  * If `idx` is negative or out of range (greater than the number of elements
  in `my_list`), the function returns the original list.
  * Without importing modules or using `try/except`.

* **3. Print a list of integers... in reverse!**
  * [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py): Python
