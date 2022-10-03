from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global dir, before_dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir[0] += 1
            elif event.key == SDLK_LEFT:
                dir[0] -= 1
            elif event.key == SDLK_UP:
                dir[1] += 1
            elif event.key == SDLK_DOWN:
                dir[1] -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir[0] -= 1
                before_dir = 1
            elif event.key == SDLK_LEFT:
                dir[0] += 1
                before_dir = -1
            elif event.key == SDLK_UP:
                dir[1] -= 1
            elif event.key == SDLK_DOWN:
                dir[1] += 1
    pass

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir = [0, 0]
before_dir = 1
frame = 0
hide_cursor()

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir[0] == 0:
        if dir[1] != 0:
            if before_dir == 1:
                character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
            elif before_dir == -1:
                character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        else:
            if before_dir == 1:
                character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
            elif before_dir == -1:
                character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    elif dir[0] == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dir[0] == -1:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    x += dir[0]

    if x+30 > TUK_WIDTH or x-30 < 0:
        print(x)
        x -= dir[0]

    y += dir[1]
    if y+40 > TUK_HEIGHT or y-50 <0:
        y -= dir[1]

close_canvas()




