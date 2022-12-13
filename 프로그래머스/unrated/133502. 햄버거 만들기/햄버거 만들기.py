from collections import deque

def solution(ingredient):
    answer = 0
    tmp = []
    
    # 1, 2, 3, 1 순서
    for n in ingredient:
        tmp.append(n)
        
        if len(tmp) >= 4 and tmp[-1] == 1:
            if tmp[-2] == 3 and tmp[-3] == 2 and tmp[-4] == 1:
                tmp.pop()
                tmp.pop()
                tmp.pop()
                tmp.pop()
                answer += 1
    
    return answer