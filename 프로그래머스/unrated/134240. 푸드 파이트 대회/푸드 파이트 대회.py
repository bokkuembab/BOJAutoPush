def solution(food):
    answer = ''
    
    for i in range(len(food)):
        answer += '%d'%i * (food[i] // 2)
        
    answer = answer + '0' + answer[::-1]
    
    return answer