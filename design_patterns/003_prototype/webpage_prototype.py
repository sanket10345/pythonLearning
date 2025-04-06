"""
WebPage Prototype Implementation

This code demonstrates the Prototype design pattern using a simple HTML page structure.
The WebPage is composed of Header, Body, and Footer components.

Each component has its own render method that returns its corresponding HTML representation.

Two types of cloning are demonstrated:
- clone(): Shallow copy where internal component references are shared
- deep_clone(): Deep copy where new instances of each component are created

This pattern is useful when object creation is expensive or when duplicating complex structures.

"""

class Header:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<header><h1>{self.content}</h1></header>'

    def clone(self):
        return Header(self.content)

class Body:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f"<main><p>{self.content}</p></main>"

    def clone(self):
        return Body(self.content)

class Footer:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f"<footer><small>{self.content}</small></footer>"

    def clone(self):
        return Footer(self.content)

class WebPage:
    def __init__(self, title, header, body, footer):
        self.title = title
        self.header = header
        self.body = body
        self.footer = footer

    # Shallow Clone (shares components)
    def clone(self):
        return WebPage(self.title, self.header, self.body, self.footer)

    # Deep Clone (creates new copies of components)
    def deep_clone(self):
        return WebPage(
            self.title,
            self.header.clone(),
            self.body.clone(),
            self.footer.clone()
        )

    def render(self):
        return f"""
<!DOCTYPE html>
<html>
<head>
  <title>{self.title}</title>
</head>
<body>
  {self.header.render()}
  {self.body.render()}
  {self.footer.render()}
</body>
</html>
""".strip()


# Test example
header = Header("Welcome to My Site")
body = Body("This is the homepage.")
footer = Footer("© 2025 MySite")

page = WebPage("Home", header, body, footer)

page2 = page.clone()
page2.header.content = 'New Header'
print(page2.header.render())   # New Header
print(page.header.render())    # Also shows New Header (shallow copy)

page3 = page.deep_clone()
page.header.content = 'Header Header Header'
print(page3.header.render())   # Old Header retained
print(page.header.render())    # New content