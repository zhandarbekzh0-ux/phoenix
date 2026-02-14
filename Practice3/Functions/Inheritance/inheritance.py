class Item:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print(self.name, self.color)

obj = Item("Ball", "Red")
obj.show()


class Box(Item):
    def __init__(self, name, color):
        pass


class Box(Item):
    def __init__(self, name, color):
        super().__init__(name, color)


class Box(Item):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.size = "Medium"


class Box(Item):
    def __init__(self, name, color, size):
        super().__init__(name, color)
        self.size = size

    def describe(self):
        print("This is a", self.color, self.name, "of size", self.size)
