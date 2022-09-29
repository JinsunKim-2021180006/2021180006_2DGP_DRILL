from pickle import FALSE
from turtle import left
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dirx,diry
    global chk

    events = get_events()
    for event in events:
        if  event.type == SDL_Quit:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                chk = 1
                dirx +=1
            elif event.key == SDLK_LEFT:
                chk = 0
                dirx -=1
            elif event.key == SDLK_UP:
                diry +=1
            elif event.key == SDLK_DOWN:
                diry -=1    
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                chk = 3
                dirx -=1
            elif event.key == SDLK_LEFT:
                chk = 2
                dirx +=1
            elif event.key == SDLK_UP:
                diry -=1
            elif event.key == SDLK_DOWN:
                diry +=1

    pass




open_canvas()
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dirx =0
diry =0
chk = 3


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * chk, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x +=dirx*5
    y +=diry*5
    delay(0.01)

close_canvas()

