def solution(s):
    answer = []
    
    for i in range(len(s)):
        tmp = s[:i]
        tmp = ''.join(reversed(tmp))
        res = tmp.find(s[i])
        answer.append(res+1 if res > -1 else res)
        
    return answer