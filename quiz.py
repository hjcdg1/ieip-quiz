STD_INPUT_HANDLE   = -10
STD_OUTPUT_HANDLE  = -11
STD_ERROR_HANDLE   = -12

FOREGROUND_BLACK     = 0x00
FOREGROUND_BLUE      = 0x01 # text color contains blue.
FOREGROUND_GREEN     = 0x02 # text color contains green.
FOREGROUND_RED       = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE      = 0x10 # background color contains blue.
BACKGROUND_GREEN     = 0x20 # background color contains green.
BACKGROUND_RED       = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

import random
import ctypes

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle) :
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool
set_color(15)

term_dict = dict()
print()
print("[1] 업무 프로세스")
print("[2] 보안")
print("[3] 데이터 통신, 인터넷")
print("[4] 모바일 컴퓨팅, 기타 신기술")
print("[5] 전체 풀기")
print()
print("풀 퀴즈의 번호를 선택하세요. : ", end="")
num = int(input())

with open(str(num) + '.txt', 'r') as f :
    while True :
        title = f.readline()    # 소제목 읽기
        if (not title) :
            break
        while True :
            line = f.readline()
            if ((not line) or (len(line) == 1)) :
                break
            line_splited = line.split(":")
            term_dict[line_splited[0]] = "".join(line_splited[1:])

while (True) :
    i = 1
    key_list = list(term_dict.keys())
    random.shuffle(key_list)
    memory = dict()
    print()
    print("<퀴즈 풀기 : " + str(len(key_list)) + "문제>")
    print()
    for term in key_list :
        print("=== Problem " + str(i).zfill(3) + " " + "="*167)  # 화면 가로 길이 넘치면 167을 더 작은 값으로 수정
        print()
        set_color(10)
        print(term_dict[term])
        set_color(15)
        print("답 보기 [Enter] ", end="")
        input()
        print()
        set_color(10)
        print("  -> " + term)
        set_color(15)
        print()
        print("다시 풀 목록에 넣기 [s], 넘어가기 [Enter] : ", end="")
        if (input() == 's') :
            memory[term] = term_dict[term]
        print()
        print("="*183)  # 화면 가로 길이 넘치면 183을 더 작은 값으로 수정
        print()
        i = i + 1
    term_dict = memory
    if (len(memory) == 0) :
        break
