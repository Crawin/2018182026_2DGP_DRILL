from pico2d import *
open_canvas()
player = load_image('penguin.png')

frame = 0
def shake_hand():
    global frame
    m_frame = frame % 8
    player.clip_draw(m_frame * 128, 128, 128, 128, 128/2, 128/2)
    pass

def birds():
    global frame
    m_frame = frame % 12
    player.clip_draw(m_frame * 128, 128 * 2, 128, 128, 128/2 + 128, 128/2)
    pass

def rope_down():
    m_frame = frame % 5
    player.clip_draw(m_frame * 128, 128 * 3, 128, 128, 128/2 + 128 * 2, 128/2)
    pass

def rope_up():
    m_frame = frame % 5 + 5
    player.clip_draw(m_frame * 128, 128 * 3, 128, 128, 128/2 + 128 * 3, 128/2)
    pass

def attack():
    m_frame = frame % 5 + 11
    player.clip_draw(m_frame * 128, 128 * 3, 128, 128, 128/2 + 128 * 4, 128/2)
    pass

def fall():
    m_frame = frame % 6 + 4
    player.clip_draw(m_frame * 128, 128 * 4, 128, 128, 128/2 + 128 * 0, 128/2 + 128)
    pass

def ghost_attack():
    m_frame = frame % 16
    player.clip_draw(m_frame * 128, 128 * 5, 128, 128, 128/2 + 128 * 1, 128/2 + 128)
    pass

def longjump():
    m_frame = frame % 8
    player.clip_draw(m_frame * 128, 128 * 6, 128, 128, 128/2 + 128 * 2, 128/2 + 128)
    pass

def shortjump():
    m_frame = frame % 4 + 8
    player.clip_draw(m_frame * 128, 128 * 6, 128, 128, 128/2 + 128 * 3, 128/2 + 128)
    pass

def idle():
    m_frame = frame % 7
    player.clip_draw(m_frame * 128, 128 * 7, 128, 128, 128/2 + 128 * 4, 128/2 + 128)
    pass

def sit_idle():
    m_frame = frame % 7 + 8
    player.clip_draw(m_frame * 128, 128 * 7, 128, 128, 128/2 + 128 * 5, 128/2 + 128)
    pass

def back_idle():
    m_frame = frame % 10
    player.clip_draw(m_frame * 128, 128 * 8, 128, 128, 128/2 + 128 * 0, 128/2 + 128 * 2)
    pass

def back_hands():
    m_frame = frame % 6
    player.clip_draw(m_frame * 128, 128 * 9, 128, 128, 128/2 + 128 * 5, 128/2)
    pass

def walk_arms():
    m_frame = frame % 6 + 6
    player.clip_draw(m_frame * 128, 128 * 9, 128, 128, 128/2 + 128 * 1, 128/2 + 128 * 2)
    pass

def walk_back():
    m_frame = frame % 6
    player.clip_draw(m_frame * 128, 128 * 10, 128, 128, 128/2 + 128 * 2, 128/2 + 128 * 2)
    pass

def walk_front():
    m_frame = frame % 6 + 6
    player.clip_draw(m_frame * 128, 128 * 10, 128, 128, 128/2 + 128 * 3, 128/2 + 128 * 2)
    pass

def walk_stop():
    m_frame = frame % 11
    player.clip_draw(m_frame * 128, 128 * 11, 128, 128, 128/2 + 128 * 4, 128/2 + 128 * 2)
    pass

def jump():
    m_frame = frame % 12
    player.clip_draw(m_frame * 128, 128 * 12, 128, 128, 128/2 + 128 * 5, 128/2 + 128 * 2)
    pass

def flip():
    m_frame = frame % 12
    player.clip_draw(m_frame * 128, 128 * 13, 128, 128, 128/2 + 128 * 0, 128/2 + 128 * 3)
    pass

def kneel_down():
    m_frame = frame % 8 + 3
    player.clip_draw(m_frame * 128, 128 * 14, 128, 128, 128/2 + 128 * 1, 128/2 + 128 * 3)
    pass

def fall_down():
    m_frame = frame % 3
    player.clip_draw(m_frame * 128, 128 * 14, 128, 128, 128/2 + 128 * 2, 128/2 + 128 * 3)
    pass

def walk():
    m_frame = frame % 9
    player.clip_draw(m_frame * 128, 128 * 15, 128, 128, 128/2 + 128 * 3, 128/2 + 128 * 3)
    pass

def fly():
    m_frame = frame % 6 + 10
    player.clip_draw(m_frame * 128, 128 * 15, 128, 128, 128/2 + 128 * 4, 128/2 + 128 * 3)
    pass

while True:
    clear_canvas()

    shake_hand()
    birds()
    rope_down()
    rope_up()
    attack()
    fall()
    ghost_attack()
    longjump()
    shortjump()
    idle()
    sit_idle()
    back_idle()
    back_hands()
    walk_arms()
    walk_back()
    walk_front()
    walk_stop()
    jump()
    flip()
    kneel_down()
    fall_down()
    walk()
    fly()

    update_canvas()
    frame += 1
    delay(0.05)
    get_events()

close_canvas()