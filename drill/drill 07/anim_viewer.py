from tkinter import Y
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character_sheet.png')

def inX():
    frame1 = 0
    for x1 in range(0,800,5):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame1*70,140,70,65,x1,90)
        update_canvas()
        frame1 = (frame1+1)%12
        delay(0.03)
        get_events()

    frame2 = 0
    frame6 = 0
    for x2 in range(0,800,5):
        clear_canvas()
        grass.draw(400,30)
        grass.draw(400,150)
        character.clip_draw(frame2*70,70,65,65,x2,90)
        character.clip_draw(frame6*70,700,65,65,x2,200)
        update_canvas()
        frame2 = (frame2+1)%10
        frame6 = (frame6+1)%7+5
        delay(0.03)
        get_events()
    

def inY():
    frame3 = 0
    frame4 = 0
    frame5 = 6
    for y1 in range(90,510,5):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame3*70,280,70,65,50,y1)
        character.clip_draw(frame4*70,420,70,65,110,y1)
        character.clip_draw(frame5*70,420,70,65,170,600-y1)
        update_canvas()
        frame3 = (frame3+1)%10
        frame4 = (frame4+1)%6
        frame5 = (frame5+1)%6+6
        delay(0.03)
        get_events()



while(True):
    inX()
    inY()
    break


close_canvas()