def solution(s):
    answer = ''
    
    for word in s.split(' '):
        for i in range(len(word)):
            answer += (word[i].lower() if i % 2 else word[i].upper())
        answer += ' '
    
    return answer[:-1]