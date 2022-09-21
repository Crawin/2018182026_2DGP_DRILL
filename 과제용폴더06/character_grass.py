from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

pos = [400,92]
runtype = True     # False 면 원운동 True 면 사각형 운동
head = 0            # 0 우측 1상단 2좌측 3 하단 방향 이동
theta = -90
while True:
    if runtype:
        while pos != [398,92]:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(pos[0],pos[1])
            if head == 0:
                pos[0] += 2
                if pos[0] >= (800 - (42 / 2)):
                    head = 1
            elif head == 1:
                pos[1] += 2
                if pos[1] >= (600 - (92 / 2)):
                    head = 2
            elif head == 2:
                pos[0] -= 2
                if pos[0] <= (42 / 2):
                    head = 3
            elif head == 3:
                pos[1] -= 2
                if pos[1] <= 92:
                    head = 0
            delay(0.01)
        pos = [400,92]
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(pos[0],pos[1])
        runtype = False
    else:
        while (theta >=-450):
            pos = [400 + 208*math.cos(math.radians(theta)), 300 + 208*math.sin(math.radians(theta))]
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(pos[0],pos[1])
            theta -= 0.5
        pos = [400,92]
        theta = -90
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(pos[0],pos[1])
        runtype = True
