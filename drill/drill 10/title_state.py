from pico2d import *
import play_state
import logo_state
import game_framework

image = None

def enter():
    global image
    image = load_image('title.png')
    pass

def exit():
    global image
    del image
    pass

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                game_framework.change_state(play_state)
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
        
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






