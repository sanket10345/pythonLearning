"""
Composite Design Pattern - File System Simulation

This script demonstrates the Composite Design Pattern using a file system structure.
In this pattern:
- 'File' represents a leaf node (no children).
- 'Folder' represents a composite node (can contain files or other folders).
- 'FileSystemRoot' acts as the root of the hierarchy and aggregates all items.

Key Features:
- Each item (File or Folder) has a `_print()` method that returns a string representation of itself.
- Folders can contain other folders and files.
- Indentation is used to visually represent depth in the hierarchy using two spaces per level.

Example Output:
Root/
  File1.txt
  Folder1/
    File2.txt

This setup allows you to treat individual objects (File) and groups of objects (Folder) uniformly,
a classic example of the Composite Pattern.
"""

class Folder:
    def __init__(self, name):
        self.name = name
        self._children = []

    def append_child(self, child):
        self._children.append(child)

    def _print(self, indent):
        output = f"{'  ' * indent}{self.name}/\n"
        for child in self._children:
            output += child._print(indent + 1)
        return output

class File:
    def __init__(self, name):
        self.name = name

    def _print(self, indent):
        return f"{'  ' * indent}{self.name}\n"

class FileSystemRoot:
    def __init__(self):
        self._children = []
        self.name = "Root"

    def append_child(self, child):
        self._children.append(child)

    def print_structure(self, indent=0):
        output = f"{self.name}/\n"
        for child in self._children:
            output += child._print(indent + 1)
        return output

# Demo usage
file_system = FileSystemRoot()

file1 = File('File1.txt')
folder1 = Folder('Folder1')
file2 = File('File2.txt')

folder1.append_child(file2)
file_system.append_child(file1)
file_system.append_child(folder1)

print(file_system.print_structure())