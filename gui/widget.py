class BaseWidget:
    def __init__(self):
        self.children = []

    def add_child(self, widget):
        self.children.append(widget)

    def render(self):
        for child in self.children:
            if hasattr(child, "render"):
                child.render()
