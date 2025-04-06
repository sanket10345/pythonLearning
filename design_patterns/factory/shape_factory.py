"""
Shape Factory Example - Demonstrating the Factory Design Pattern with Shapes

This script uses the Factory Design Pattern to create and draw different types of shapes.

Components:
1. `Shape` - Abstract base class that defines a common interface with the `draw()` method.
2. `Circle`, `Rectangle`, `Square` - Concrete shape classes that implement the `draw()` method.
3. `ShapeFactory` - Provides the `get_shape()` method to create instances of shapes based on a string input.

Usage:
- Use the `ShapeFactory` to request a shape by name (e.g., "circle", "square").
- Each shape object implements its own `draw()` method, encapsulating its drawing logic.

This pattern is useful for decoupling the object creation process from the main logic and
makes it easy to add new shapes without modifying the client code or the factory interface.

Example Output:
Drawing a Circle  
Drawing a Square  
Drawing a Rectangle
"""

class Shape:
    def draw(self):
        pass

class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
        if shape_type == "rectangle":
            return Rectangle()
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

circle = ShapeFactory().get_shape('circle')
circle.draw()
square = ShapeFactory().get_shape('square')
square.draw()
rectangle = ShapeFactory().get_shape('rectangle')
rectangle.draw()
