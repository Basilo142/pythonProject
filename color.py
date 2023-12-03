from dataclasses import dataclass


@dataclass
class Color:
    x: int = None
    y: int = None
    z: int = None

    def black(self):
        self.x = 0
        self.y = 0
        self.z = 0
        return self.x, self.y, self.z

    def white(self):
        self.x = 255
        self.y = 255
        self.z = 255
        return self.x, self.y, self.z

    def gray(self):
        self.x = 128
        self.y = 128
        self.z = 128
        return self.x, self.y, self.z

    def red(self):
        self.x = 255
        self.y = 0
        self.z = 0
        return self.x, self.y, self.z

    def yellow(self):
        self.x = 255
        self.y = 255
        self.z = 0
        return self.x, self.y, self.z

    def aqua(self):
        self.x = 0
        self.y = 255
        self.z = 255
        return self.x, self.y, self.z


colors = Color()
