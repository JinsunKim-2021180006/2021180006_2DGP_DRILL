import math
from pico2d import *

open_canvas()

glass = load_image('grass.png')
character = load_image('character.png')

def rec_move():
    x=0
    y=90
    while(x<750):
        clear_canvas_now()
        glass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+2
        delay(0.001)
    while(y<540):
        clear_canvas_now()
        glass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+2
        delay(0.001)
    while(x>40):
        clear_canvas_now()
        glass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        delay(0.001)
    while(y>90):
        clear_canvas_now()
        glass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        delay(0.001)
    while(x<400):
        clear_canvas_now()
        glass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+2
        delay(0.001)
    


def cicle_move():
    x=400
    y=90
    r=0
    while(r<6):
        clear_canvas_now()
        glass.draw_now(400,30)
        character.draw_now(x,y)
        x= 400+ math.cos(r)*230
        y= 300+math.sin(r)*230
        r=r+0.1
        delay(0.1)

while(True):
    rec_move()
    cicle_move()
close_canvas()
