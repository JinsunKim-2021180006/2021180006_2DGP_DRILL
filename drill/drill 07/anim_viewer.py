from tkinter import Frame
from turtle import update
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character_sheet.png')

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
x2=0

for x2 in range(0,800,5):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame2*70,70,65,65,x2,90)
    update_canvas()
    frame2 = (frame2+1)%10
    delay(0.03)
    get_events()

close_canvas()