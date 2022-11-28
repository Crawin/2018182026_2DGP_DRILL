import game_framework
from pico2d import *

import game_world
import server

import random

class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1817), random.randint(0, 1056)

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.clip_draw(0, 0, 21, 21, sx, sy)
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 21/2, self.y - 21/2, self.x + 21/2, self.y + 21/2

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)