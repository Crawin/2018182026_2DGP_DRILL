from pico2d import *

class Grass:
    def __init__(self, x, y):
        self.image = load_image('grass.png')
        self.pos = [x, y]

    def draw(self):
        self.image.draw(self.pos[0], self.pos[1])

    def update(self):
        pass
