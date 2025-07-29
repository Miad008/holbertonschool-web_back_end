# Python Variable Annotations Project

This project focuses on understanding and using **Python Type Annotations** effectively. It includes a series of tasks designed to practice working with **type annotations**, **functions**, **type hinting**, and **Python's `asyncio` module** for asynchronous programming.

## Tasks Overview

1. **Task 0: Basic annotations - add**
    - **Objective**: Implement a function `add` that takes two `float` arguments and returns their sum as a `float`.
    - **Concepts**: Type annotations, function implementation.

2. **Task 1: Basic annotations - concat**
    - **Objective**: Write a function `concat` that takes two strings and returns their concatenation as a string.
    - **Concepts**: Type annotations, string operations.

3. **Task 2: Basic annotations - floor**
    - **Objective**: Write a function `floor` that takes a float `n` as an argument and returns the floor of the float as an integer.
    - **Concepts**: Type annotations, using `math.floor()`.

4. **Task 3: Basic annotations - to string**
    - **Objective**: Write a function `to_str` that takes a float `n` as an argument and returns the string representation of the float.
    - **Concepts**: Type annotations, string conversion.

5. **Task 4: Define variables**
    - **Objective**: Define and annotate the following variables:
      - `a`: An integer with a value of 1.
      - `pi`: A float with a value of 3.14.
      - `i_understand_annotations`: A boolean with a value of `True`.
      - `school`: A string with a value of `"Holberton"`.
    - **Concepts**: Variable annotation.

6. **Task 5: Complex types - list of floats**
    - **Objective**: Write a function `sum_list` that takes a list of floats as an argument and returns their sum as a float.
    - **Concepts**: Type annotations, list operations.

7. **Task 6: Complex types - mixed list**
    - **Objective**: Write a function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float.
    - **Concepts**: Type annotations, handling mixed data types in lists.

8. **Task 7: Complex types - string and int/float to tuple**
    - **Objective**: Write a function `to_kv` that takes a string `k` and an integer or float `v`, and returns a tuple where the first element is the string and the second is the square of `v`.
    - **Concepts**: Type annotations, using tuples and performing arithmetic operations.

9. **Task 8: Complex types - functions**
    - **Objective**: Write a function `make_multiplier` that takes a float `multiplier` as an argument and returns a function that multiplies a float by `multiplier`.
    - **Concepts**: Type annotations, higher-order functions, closures.

10. **Task 9: Let's duck type an iterable object**
    - **Objective**: Annotate the `element_length` function, which takes an iterable object and returns a list of tuples where each tuple contains an element and its length.
    - **Concepts**: Type annotations, working with iterable and sequence objects.

## Requirements

- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- Your code should be written using **pycodestyle** (version 2.5.x).
- All functions, coroutines, and modules must be properly annotated with types (type hinting).
- All your modules must have appropriate documentation.
- You should make use of the **random module** and **`asyncio`** for certain tasks (especially for later tasks).
- Ensure that all your code is executable.

## Setup

1. Clone the repository.
2. Ensure that you are using Python 3.9 or higher.
3. Run the scripts using:

```bash
python3 <script_name>.py
