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

i = 1
key_list = list(term_dict.keys())
random.shuffle(key_list)
memory = dict()
for term in key_list :
    print("### Problem " + str(i).zfill(3) + "#"*167)
    print()
    print(term_dict[term])
    print("답을 보려면 아무 키나 누르세요. : ", end="")
    input()
    print()
    print("답 :", term)
    print()
    print("기억 상자에 넣으시겠습니까? (y/n) : ", end="")
    print("#"*182)
    print()
    i = i + 1
