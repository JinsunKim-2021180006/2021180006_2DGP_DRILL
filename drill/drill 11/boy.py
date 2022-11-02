from pico2d import *

PI = 3.141592

RD,LD,RU,LU, Key_A, TIMER = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN,SDLK_a): Key_A
}

class IDLE: 
    @staticmethod
    def enter(self,event):
        print("enter idle")
        self.dir = 0
        self.timer = 1000
        pass

    @staticmethod
    def exit(self):
        print("exit idle")
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame+1)%1
        self.timer -= 1
        if self.timer == 0:#시간이 경과하면
            # 이벤트를 발생시켜줘야한다. TIMER
            # 객체지향 프로그래밍 위배...
            self.add_event(TIMER)
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1: #오른쪽을 바라보고 있는 상태
            self.image.clip_draw(self.frame*100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 200, 100, 100, self.x, self.y)
       
        pass

class RUN:
    def enter(self,event):
        print('enter run')
        if event == RD:
            self.dir +=1
        elif event == LD:
            self.dir -=1
        elif event == RU:
            self.dir -=1
        elif event == LU:
            self.dir +=1

    def exit(self):
        print("exit run")
        #run 을 나갈, ible로 갈때. run의 방향을 알려줄 필요가 있다.
        self.face_dir =self.dir
        pass

    def do(self):
        self.frame = (self.frame +1)%8
        self.x += self.dir
        self.x = clamp(0,self.x,800)
        pass

    def draw(self):
        print("draw run")
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
               
        pass

class SLEEP:
    def enter(self, event):
        print("enter sleep")
        self.frame = 0
        pass

    def exit(self):
        pass
    
    def do(self):
        self.frame = (self.frame+1)%1

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame*100, 300, 100, 100, 
                PI/2,'',
                self.x, self.y-25,100,100)
        else:
            self.image.clip_composite_draw(self.frame*100, 200, 100, 100, 
                -PI/2,'',
                self.x, self.y-25,100,100)
       
class AUTO_RUN:
    def enter(self,event):
        if self.face_dir == 1:
            self.dir +=1
        elif self.face_dir == -1:
            self.dir -=1
        self.frame = 0
        print('enter auto run')


    def exit(self):
        print("exit auto run")
        self.face_dir = self.dir
        pass

    def do(self):

      
        self.frame = (self.frame +1)%8
        self.x += self.dir*1
        if self.x >= 800:
            self.dir =-1
            self.x=800
        elif self.x <= 0:
            self.dir = 1
            self.x = 0

        self.x = clamp(0,self.x,800)

        
        pass

    def draw(self):
        print("draw run")
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
               
        pass


next_state = {
    IDLE: {RD:RUN,LD:RUN,RU:RUN,LU:RUN, TIMER:SLEEP, Key_A:AUTO_RUN},
    RUN: {RD:IDLE,LD:IDLE,RU:IDLE,LU:IDLE,Key_A:AUTO_RUN},
    SLEEP: {RD:RUN,LD:RUN,RU:RUN,LU:RUN},
    AUTO_RUN: {RD:RUN,LD:RUN,RU:RUN,LU:RUN, Key_A:IDLE}
}

class Boy:
    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.timer = 100

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

    def update(self):
        self.cur_state.do(self)
        
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self,event)


    def draw(self):
        self.cur_state.draw(self) 
        

    def add_event(self,event):
        self.q.insert(0,event)
        
    def handle_event(self,event):
       if (event.type,event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
       