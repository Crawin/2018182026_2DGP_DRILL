import pico2d
from pico2d import *
import game_framework
import play_state
import title_state

# running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('add_delete_boy.png')

def exit():
    global image
    del image

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()  # 이전 상태인 play_state로 복귀
                case pico2d.SDLK_j:
                    play_state.boy.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_k:
                    if len(play_state.boy) > 1:
                        del play_state.boy[-1]
                    game_framework.pop_state()