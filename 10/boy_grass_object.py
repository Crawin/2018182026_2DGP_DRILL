from pico2d import *
from random import randint as rand
# 잔디를 만드려면, 잔디 클래스가 필요
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

# 소년을 만드려면, 소년 클래스가 필요.
class Boy:
    def __init__(self):
        self.x, self.y = rand(100, 700), 90
        self.frame = rand(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
team = [Boy() for i in range(11)]
grass = Grass()

running = True
# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)

# finalization code
for boy in team:
    del boy
del grass
close_canvas()
