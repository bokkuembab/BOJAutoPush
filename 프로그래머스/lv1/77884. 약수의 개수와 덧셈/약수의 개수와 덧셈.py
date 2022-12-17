def solution(left, right):
    answer = 0
    
    for n in range(left, right + 1):
        if int(n ** 0.5) == n ** 0.5:
            answer -= n
        else:
            answer += n
    
    return answer