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

## Author

**Engr. Dr. Malik Abdal Salam**
