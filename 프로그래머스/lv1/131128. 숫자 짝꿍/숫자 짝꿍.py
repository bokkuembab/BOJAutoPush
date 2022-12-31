def solution(X, Y):
    answer = ''
    
    for i in range(9, -1, -1):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))
        
    if not answer:
        answer = "-1"
    elif len(answer) == answer.count('0'):
        answer = "0"
    else:
        answer = "".join(sorted(answer, reverse=True))
        
    return answer