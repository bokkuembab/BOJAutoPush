from collections import deque

def solution(ingredient):
    answer = 0
    tmp = []
    
    # 1, 2, 3, 1 순서
    for n in ingredient:
        tmp.append(n)
        
        if tmp[-4:] == [1,2,3,1]:
            answer += 1
            for i in range(4):
                tmp.pop()
    
    return answer