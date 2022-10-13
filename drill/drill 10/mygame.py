import game_framework
import pico2d
import logo_state
import play_state
import title_state

state = [
    logo_state,
    title_state,
    play_state
    ]

pico2d.open_canvas()
game_framework.run(state[2])
pico2d.close_canvas()
