"""
classlog_class_decorator.py

This script demonstrates a **class-level decorator** in Python that automatically
logs every method call within a decorated class.

Decorator Type:
- Class Decorator (applied to a class, not a function)
- Internally uses a wrapper to intercept method calls
- Logs method name, arguments, and return value

How It Works:
- The `ClassLogDecorator` accepts a class during initialization.
- When the class is instantiated, it wraps all instance methods (excluding dunder methods)
  with a logging function.
- Each method call will print:
    - Method name
    - Arguments (both positional and keyword)
    - Return value

Use Case:
- Debugging classes with many methods
- Auditing method calls
- Teaching/tracing object behavior

Example Usage:
    @ClassLogDecorator
    class MathOps:
        def add(self, x, y):
            return x + y

    math = MathOps()
    math.add(2, 3)

Expected Output:
    Calling add with args: (<MathOps object>, 2, 3), kwargs: {}
    add returned: 5

Limitations:
- Only instance methods are wrapped.
- Does not wrap static or class methods by default.

"""

class ClassLogDecorator:
    def __init__(self, cls):
        self.cls = cls  # Store the original function

    def log_wrapper(self, func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        return wrapper
        
    def __call__(self, *args, **kwargs):
        # Create a new instance of the class
        obj = self.cls(*args, **kwargs)

        # Loop through all attributes of the class
        for attr_name in dir(obj):
            if attr_name.startswith("__"):
                continue  # Skip dunder methods

            attr = getattr(obj, attr_name)
            if callable(attr):
                # Wrap method with log_wrapper
                wrapped = self.log_wrapper(attr)
                setattr(obj, attr_name, wrapped)

        return obj

@ClassLogDecorator
class MathOps:
    def add(self, x, y): 
        return x + y
    def mul(self, x, y):
        return x * y
    def sub(self, x, y):
        return x - y
    def div(self, x, y):
        return x / y
    def pow(self, x, y):
        return x ** y  # corrected from division to power

mathop = MathOps()
mathop.add(2, 3)
mathop.mul(3, 4)