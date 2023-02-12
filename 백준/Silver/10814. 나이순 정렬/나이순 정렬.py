import sys

mem_num = int(sys.stdin.readline())    # mem_num: 회원의 수

mem_li = []    # mem_li: 회원 리스트: [(나이, 이름), ... ] 형식

for _ in range(mem_num):
    mem_li.append(tuple(sys.stdin.readline().split()))
    
# 나이, 가입한 순으로 정렬 
# (key에 나이만 입력->나이만 정렬기준으로 정렬하므로 나이 기준 정렬 후, 저장된 순서대로 출력됨)
mem_li.sort(key=lambda m: int(m[0]))    

for age, name in mem_li:    # 출력: (나이 이름) 형식
    print(age, name)