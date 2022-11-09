from pico2d import *
import game_framework
import game_world
import random
from ball import Ball

#1 : 이벤트 정의
RD, LD, RU, LU, TIMER, SPACE = range(6)
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'SPACE']


# 새 속력 계산
PIXEL_PER_METER = (10/0.3)
RUN_SPEED_KMPH = 10 #마라토너의 평속
RUN_SPEED_MPM = (RUN_SPEED_KMPH *1000/60)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 새 Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        if self.face_dir == 1:
            self.dir +=1
        elif self.face_dir == -1:
            self.dir -=1
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        if event == SPACE:
            self.fire_ball()

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 5
        if self.x >= 1600:
            self.dir =-1
            self.x=1600
        elif self.x <= 0:
            self.dir = 1
            self.x = 0
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time



    @staticmethod
    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(self.frame * 183, 168*2, 183, 168, 0, '', self.x, self.y,100,100)
        elif self.dir == -1:
            self.image.clip_composite_draw(self.frame * 183, 168*2, 183, 168, 0, 'h', self.x, self.y,100,100)


#3. 상태 변환 구현

next_state = {
    IDLE: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE},
}




class Bird:

    def __init__(self,x,y):
        self.x, self.y = x, y
        self.frame = random.randint(0,4)
        self.dir, self.face_dir = 0, 1
        self.image = load_image('bird_animation.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        self.font = load_font('ENCR10B.TTF',16)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fire_ball(self):
        print('FIRE BALL')
        ball = Ball(self.x, self.y, self.face_dir*2)
        game_world.add_object(ball, 1)
