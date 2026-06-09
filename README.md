# #######################################################

# 📢📢  Attention Please 📢📢
## New Assignment has beed added in "Tasks" folder
# #######################################################
____________________________________________________________________________________________________________
# Python Loops and Control Statements

This repository contains examples and explanations of Python's **for loop**, **while loop**, and **break statement**.

## Table of Contents

1. Introduction
2. For Loop
3. While Loop
4. Break Statement
5. Examples
6. Practice Exercises

---

# Introduction

Loops allow a program to execute a block of code multiple times.

- **for loop** – Used when the number of iterations is known.
- **while loop** – Used when the number of iterations depends on a condition.
- **break statement** – Used to terminate a loop immediately.

---

# For Loop

## Syntax

```python
for variable in sequence:
    # code block
```

## Example

```python
for i in range(1, 6):
    print(i)
```

---

# While Loop

## Syntax

```python
while condition:
    # code block
```

## Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Break Statement

## Example

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

---

# Practice Exercises

1. Print numbers from 1 to 20 using a for loop.
2. Print even numbers from 2 to 20 using a for loop.
3. Print numbers from 10 down to 1 using a while loop.
4. Create a password checker using a while loop.
5. Stop a loop when a number reaches 6 using break.

---

# Python Functions: Theory & Examples

## 1. What is a Function?

A **function** is a reusable block of code that performs a specific task. Functions help break complex problems into smaller, manageable pieces, avoid code repetition, and improve program organization.

### Why Use Functions?
- **Modularity**: Divide a large task into smaller logical steps
- **Reusability**: Write once, use many times
- **Abstraction**: Hide complex logic behind a simple call
- **Maintainability**: Fix a bug in one place, not everywhere

---

## 2. Defining a Function

Use the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`.

### Syntax

`def function_name(parameters):`
    `"""Optional docstring: explains what the function does"""`
    `# Function body`
    `return value  # Optional`

### Example

`def greet():`
    `"""Prints a simple greeting"""`
    `print("Hello, World!")`

`# Call the function`
`greet()  # Output: Hello, World!`

---

## 3. Function Parameters and Arguments

### 3.1 Positional Arguments
Arguments are passed in the correct order.

`def add(a, b):`
    `return a + b`

`result = add(3, 5)  # a=3, b=5`
`print(result)       # Output: 8`

### 3.2 Default Parameters
Assign default values to parameters.

`def greet_user(name, greeting="Hello"):`
    `return f"{greeting}, {name}!"`

`print(greet_user("Alice"))          # Output: Hello, Alice!`
`print(greet_user("Bob", "Hi"))      # Output: Hi, Bob!`

> **Important**: Default parameters must come after non-default parameters.

### 3.3 Keyword Arguments
Specify arguments by parameter name.

`def describe_person(name, age, city):`
    `return f"{name} is {age} years old and lives in {city}."`

`print(describe_person(city="Paris", age=30, name="Eve"))`
`# Output: Eve is 30 years old and lives in Paris.`

### 3.4 Variable-Length Arguments

- `*args` – for an arbitrary number of positional arguments (tuple)
- `**kwargs` – for an arbitrary number of keyword arguments (dictionary)

`def sum_all(*args):`
    `return sum(args)`

`print(sum_all(1, 2, 3, 4))  # Output: 10`

`def print_info(**kwargs):`
    `for key, value in kwargs.items():`
        `print(f"{key}: {value}")`

`print_info(name="Alice", age=25, job="Engineer")`
`# Output:`
`# name: Alice`
`# age: 25`
`# job: Engineer`

---

## 4. The `return` Statement

A function can send a value back to the caller using `return`. Without `return`, the function returns `None`.

`def square(x):`
    `return x * x`

`result = square(5)`
`print(result)  # Output: 25`

`def no_return():`
    `x = 5`

`print(no_return())  # Output: None`

### Returning Multiple Values

`def get_min_max(numbers):`
    `return min(numbers), max(numbers)`

`minimum, maximum = get_min_max([4, 2, 9, 1, 6])`
`print(minimum, maximum)  # Output: 1 9`

---

## 5. Scope of Variables

- **Local scope**: Variables defined inside a function are accessible only within that function
- **Global scope**: Variables defined outside all functions are accessible everywhere

`x = 10  # Global variable`

`def my_func():`
    `y = 5   # Local variable`
    `print(x)  # Can access global (read-only by default)`

`my_func()      # Output: 10`
`# print(y)     # Error: y is not defined outside the function`

### Modifying Global Variables
Use the `global` keyword.

`counter = 0`

`def increment():`
    `global counter`
    `counter += 1`

`increment()`
`print(counter)  # Output: 1`

---

## 6. Lambda Functions (Anonymous Functions)

Small, one-line functions defined with the `lambda` keyword. They can have any number of arguments but only one expression.

### Syntax

`lambda arguments: expression`

### Example

`square = lambda x: x ** 2`
`print(square(5))  # Output: 25`

`# Common use with sorted, filter, map`
`numbers = [1, 2, 3, 4, 5]`
`squared = list(map(lambda x: x ** 2, numbers))`
`print(squared)  # Output: [1, 4, 9, 16, 25]`

`even = list(filter(lambda x: x % 2 == 0, numbers))`
`print(even)     # Output: [2, 4]`

---

## 7. Docstrings (Documentation)

A string literal immediately after the function definition. Use triple quotes for multi-line docstrings.

`def multiply(a, b):`
    `"""`
    `Returns the product of two numbers.`

    `Parameters:`
    `a (int, float): The first number`
    `b (int, float): The second number`

    `Returns:`
    `int or float: The product of a and b`
    `"""`
    `return a * b`

`print(multiply.__doc__)   # View docstring`
`help(multiply)            # Another way`

---

## 8. Recursive Functions

A function that calls itself. Must have a base case to stop recursion.

`def factorial(n):`
    `"""Compute n! recursively"""`
    `if n == 0:      # Base case`
        `return 1`
    `else:           # Recursive case`
        `return n * factorial(n - 1)`

`print(factorial(5))  # Output: 120`

---

## 9. Built-in Functions (Common Examples)

| Function | Description | Example |
|----------|-------------|---------|
| `len()` | Returns length of object | `len([1,2,3])` → `3` |
| `type()` | Returns data type | `type(5)` → `<class 'int'>` |
| `print()` | Outputs to console | `print("Hi")` |
| `input()` | Reads user input | `name = input("Name: ")` |
| `range()` | Generates sequence | `list(range(3))` → `[0,1,2]` |
| `sum()` | Sums an iterable | `sum([1,2,3])` → `6` |
| `max()` / `min()` | Finds max/min value | `max(5, 2, 8)` → `8` |

---

## 10. Quick Summary Table

| Concept | Syntax Example |
|---------|----------------|
| Definition | `def my_func():` |
| Parameters | `def add(a, b):` |
| Default param | `def greet(name="User"):` |
| Return value | `return result` |
| Multiple returns | `return a, b` |
| Lambda | `lambda x: x*2` |
| Docstring | `"""Description"""` |
| *args | `def func(*args):` |
| **kwargs | `def func(**kwargs):` |

---

## 11. Common Mistakes to Avoid

1. **Forgetting the colon** after function definition
2. **Mixing up parameters** order in positional arguments
3. **Modifying a global variable** without using `global`
4. **No return statement** when a value is expected (returns `None`)
5. **Infinite recursion** – always include a base case
6. **Using mutable default arguments** (can cause bugs)

### Bad Example: Mutable Default Argument

`def add_item(item, lst=[]):`
    `lst.append(item)`
    `return lst`

`print(add_item(1))  # [1]`
`print(add_item(2))  # [1, 2] ← Unexpected!`

### Good Example: Use None Instead

`def add_item(item, lst=None):`
    `if lst is None:`
        `lst = []`
    `lst.append(item)`
    `return lst`

`print(add_item(1))  # [1]`
`print(add_item(2))  # [2]`

---

## 12. Practice Exercises

1. Write a function that takes a list of numbers and returns the average
2. Create a recursive function to calculate Fibonacci numbers
3. Write a lambda function to check if a number is even
4. Create a function with `*args` that finds the maximum value
5. Write a function with a docstring that converts temperature from Celsius to Fahrenheit

---

**End of Python Functions Theory**

## Author

**Engr. Dr. Malik Abdal Salam**
