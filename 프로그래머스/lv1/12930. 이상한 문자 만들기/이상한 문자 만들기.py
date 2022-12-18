def solution(s):
    answer = ''
    
    for word in s.split(' '):
        for i in range(len(word)):
            answer += (word[i].upper() if i % 2 == 0 else word[i].lower())
        answer += ' '
    
    return answer[:-1]