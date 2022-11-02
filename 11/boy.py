from pico2d import *

# RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, aD, aU = range(7)

# 키 입력확인을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT)   : RD,
    (SDL_KEYDOWN, SDLK_LEFT)    : LD,
    (SDL_KEYUP, SDLK_RIGHT)     : RU,
    (SDL_KEYUP, SDLK_LEFT)      : LU,
    (SDL_KEYDOWN, SDLK_a)   : aD,
}

class IDLE:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000
        pass
    def exit(self): # 상태를 나올 때 행하는 액션, 고개 들기
        print('EXIT IDLE')
        pass
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer <= 0:
            self.add_event(TIMER)
        pass
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

class SLEEP:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('ENTER SLEEP')
        pass
    def exit(self): # 상태를 나올 때 행하는 액션, 고개 들기
        print('EXIT SLEEP')
        pass
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        pass
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592/2, '', self.x + 25, self.y- 25, 100 ,100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592/2, '', self.x-25, self.y-25,100,100)

class RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN')
        # 방향을 결정해야 하는데, 어떤 키가 눌렸기 때문에?
        # 키 이벤트 정보가 필요
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class AUTO_RUN:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('ENTER AUTO_RUN')
        self.dir = self.face_dir
        pass
    def exit(self): # 상태를 나올 때 행하는 액션, 고개 들기
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir
        self.dir = 0
        pass
    def do(self): # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x != clamp(0, self.x, 800):
            self.dir = self.dir * -1
        self.x = clamp(0, self.x, 800)

        pass
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y+25,200,200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y+25,200,200)

#3. 상태 변환 기술
next_state = {
    AUTO_RUN: {aD: IDLE, RD: RUN, LD: RUN, RU: RUN, LU: RUN},
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, TIMER: SLEEP, aD: SLEEP},
    IDLE: {RU: RUN,    LU: RUN, RD: RUN,    LD: RUN, TIMER: SLEEP, aD: AUTO_RUN},
    RUN:  {RU: IDLE,   LU: IDLE, RD: IDLE,   LD: IDLE, aD: AUTO_RUN}
}


class Boy:
    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir += 1
        #             boy.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir -= 1
        #             boy.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = [] # 이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) # 초기 상태의 entry 액션 수행

    def update(self):
        self.cur_state.do(self) # 현재 상태의 do 액션 수행
        #이벤트를 확인해서, 이벤트가 있으면 이벤트 변환 처리
        if self.q: #큐에 이벤트가 있으면
            event = self.q.pop()
            self.cur_state.exit(self) # 현재 상태를 나가야하고,
            self.cur_state = next_state[self.cur_state][event] # 다음 상태를 구한다.
            self.cur_state.enter(self, event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)