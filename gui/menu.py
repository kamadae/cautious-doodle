class Menu:
    """Simple text menu used in the demo."""

    def __init__(self, title, options):
        self.title = title
        self.options = options

    def open(self):
        """Print the menu and return the selected option index."""
        print(self.title)
        for i, opt in enumerate(self.options, 1):
            print(f" {i}. {opt}")
        choice = input("Select option: ")
        try:
            return int(choice) - 1
        except ValueError:
            return -1
