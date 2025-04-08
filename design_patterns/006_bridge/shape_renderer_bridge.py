"""
🎯 Bridge Pattern Example – Rendering Shapes

This script demonstrates the Bridge Design Pattern using a shape rendering example.
The goal is to decouple the abstraction (Shape) from its implementation (Renderer),
so they can vary independently.

🧱 Components:

1. Shape (Abstract Class)
   - Takes a Renderer object via constructor (acts as the "bridge").
   - Subclasses (Triangle, Square) define the `name` property only.
   - `__str__` uses both shape name and renderer output to produce the final result.

2. Renderer (Interface)
   - Defines a `what_to_render_as` property.
   - Concrete implementations:
     - RasterRenderer → returns 'pixels'
     - VectorRenderer → returns 'lines'

✅ Advantages:
- Easily add new shapes or rendering styles without modifying existing code.
- Avoids class explosion (e.g., RasterTriangle, VectorSquare, etc.).
- Clean separation of concerns: "what to draw" vs. "how to draw it".

📦 Example Output:
- Drawing Triangle as pixels
- Drawing Square as lines

Perfect use case when combining multiple dimensions of variation (e.g., shapes and styles).
"""

class Shape:

    def __init__(self, renderer):
        self.renderer = renderer
    @property
    def name(self):
        pass

    def __str__(self):
        return f'Drawing {self.name} as {self.renderer.what_to_render_as}'

# Concrete Shapes
class Triangle(Shape):
    @property
    def name(self):
        return 'Triangle'

class Square(Shape):
    @property
    def name(self):
        return 'Square'


class Renderer():
    @property
    def what_to_render_as(self):
        return None

class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'

class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'

print(str(Triangle(RasterRenderer())))  # ➝ "Drawing Triangle as pixels"
print(str(Square(VectorRenderer())))    # ➝ "Drawing Square as lines"