"""
log_decorator_functional.py

This script demonstrates a **functional decorator** in Python.
The `@log` decorator wraps a function and logs its name, arguments,
and return value every time it is called.

Decorator Type: Functional (uses closures)

Use Case:
- Logging function calls for debugging or monitoring
- Easily reusable across multiple functions

Example:
    @log
    def add(x, y):
        return x + y

    add(2, 3)

Expected Output:
    Calling add(2, 3)
    Output of add(2, 3): 5
"""

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"Output of {func.__name__}{args}: {result}")
        return result
    return wrapper

@log
def add(x, y):
    return x + y

# Now just call once
add(2, 3)