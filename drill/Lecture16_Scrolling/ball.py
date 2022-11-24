from pico2d import *
import game_world
import server

class Ball:
    image = None

    def __init__(self, x, y):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

        self.w = 23
        self.h = 23
        self.x,self.y=x,y

    def draw(self):
        self.image.clip_draw_to_origin(0,0,23,23,self.x,self.y)


    def update(self):
        self.x +=server.boy.x
        self.y += server.boy.y
        # self.x = clamp(0, (int)(server.boy.x) - self.canvas_width//2,800)
        # self.y = clamp(0, (int)(server.boy.y) - self.canvas_height//2,600)

        pass