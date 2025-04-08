"""
repeat_decorator_dynamic.py

This script demonstrates a **dynamic functional decorator** in Python.
The `repeat` function acts as a decorator that repeats the execution
of another function a specified number of times.

Decorator Type: Functional (dynamic application)

Usage:
Instead of using @ syntax, the decorator is applied at runtime:

    repeater = repeat(say_hello, count=3)
    repeater()

Features:
- Dynamically wraps any function and calls it N times.
- Logs each repetition index and output (if any).
- Useful for testing, repeated calls, animations, or simulation loops.

Note:
- If the decorated function does not return anything, `None` will be printed.
- To suppress output, remove or modify the `print(f"{i}: {result}")` line.
"""

def repeat(func,count):
    def wrapper(*args, **kwargs):
        for i in range(0,count):
            print(f"Execution Number: {i+1}")
            result = func(*args, **kwargs)
        return result
    return wrapper

def say_hello():
    print("Hello")

# Apply the decorator dynamically (not with @)
repeater = repeat(say_hello, count=3)
repeater()