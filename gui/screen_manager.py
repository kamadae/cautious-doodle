class ScreenManager:
    def __init__(self):
        self.screens = []

    def push(self, screen):
        self.screens.append(screen)

    def pop(self):
        if self.screens:
            self.screens.pop()

    def current(self):
        if self.screens:
            return self.screens[-1]
        return None
