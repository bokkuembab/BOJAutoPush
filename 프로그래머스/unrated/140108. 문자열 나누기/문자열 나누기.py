from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    
    while s:
        x = s.popleft()
        if not s:
            answer += 1
            break
        
        if x != s.popleft():
            answer += 1
            continue
            
        times = 2
        while (times > 0) and s:
            if x == s.popleft():
                times += 1
            else:
                times -= 1
        answer += 1
    
    return answer