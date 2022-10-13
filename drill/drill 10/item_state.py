from pico2d import *
import game_framework
import play_state

image = None



#게임 초기화
def enter():
    global image
    

#종료 - 객체를 소멸
def exit():
    global image
    del image

def update():
    #게임월드에 객체를 업데이트 - 게임로직
    global image
    image =load_image('add_delete_boy.png')
    pass



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
            
                case pico2d.SDLK_0:
                    play_state.boy.item = None
                    game_framework.pop_state()

                case pico2d.SDLK_1:
                    play_state.boy.item = 'Ball'
                    game_framework.pop_state()

                case pico2d.SDLK_2:
                    play_state.boy.item = 'BigBall'
                    game_framework.pop_state()
                    
                    
                case pico2d.SDLK_3:
                    play_state.n += 1
                    game_framework.pop_state()
                    
                case pico2d.SDLK_4:
                    if play_state.n>=1:
                        play_state.n -= 1
                    game_framework.pop_state()
                    



def draw():
    #게임월드 랜더링
    clear_canvas()
    play_state.enter()
    image.draw(400,300)
    update_canvas()


#단독 실행 코드
def test_self():
    import sys
    this_module = sys.modules['__main__']

    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': #만약 단독 실행 상태이면
    test_self()




