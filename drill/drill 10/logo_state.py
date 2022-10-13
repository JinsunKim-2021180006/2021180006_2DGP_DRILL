from pico2d import *
import play_state
import title_state
import game_framework

image = None
logo_time =0.01


def enter():
    global image, logo_time
    logo_time =0.01
    image = load_image('tuk_credit.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    global logo_time
    if logo_time>1.0:
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time+=0.01

    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()





