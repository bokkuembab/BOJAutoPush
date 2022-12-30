def solution(food):
    answer = ''
    
    for i,n in enumerate(food):
        answer += str(i) * (n // 2)
        
    answer = answer + '0' + answer[::-1]
    
    return answer