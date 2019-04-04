import random

term_dict = dict()
with open('quiz1.txt', 'r') as f :
    while True :
        title = f.readline()    # 소제목 읽기
        if (not title) :
            break
        while True :
            line = f.readline()
            if ((not line) or (len(line) == 1)) :
                break
            line_splited = line.split(":")
            term_dict[line_splited[0]] = line_splited[1]
'''
for term in term_dict.keys() :
    print(term + ":" + term_dict[term])
'''

while (True) :
    i = 1
    key_list = list(term_dict.keys())
    random.shuffle(key_list)
    memory = dict()
    print()
    print("퀴즈 풀기 : " + str(len(key_list)) + "문제")
    print()
    for term in key_list :
        print("### Problem " + str(i).zfill(3) + " " + "#"*167)
        print()
        print(term_dict[term])
        print("답을 보려면 아무 키나 누르세요. : ", end="")
        input()
        print()
        print("답 :", term)
        print()
        print("저장하고 싶으면 s를 누르세요. : ", end="")
        if (input() == 's') :
            memory[term] = term_dict[term]
        print()
        print("#"*182)
        print()
        i = i + 1
    term_dict = memory
    if (len(memory) == 0) :
        break
