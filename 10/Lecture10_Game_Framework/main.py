import pico2d
import play_state
import logo_state

start_state = logo_state # 모듈을 변수로 취급.


pico2d.open_canvas()

# start_state.enter()
# # game main loop code
# while start_state.running:
#     start_state.handle_events()
#     start_state.update()
#     start_state.draw()
#     pico2d.delay(0.05)
# start_state.exit()
#
# start_state = play_state
# start_state.enter()
# # game main loop code
# while start_state.running:
#     start_state.handle_events()
#     start_state.update()
#     start_state.draw()
#     pico2d.delay(0.05)
# start_state.exit()

states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
    state.exit()

pico2d.close_canvas()

# finalization code
pico2d.close_canvas()