def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            continue
        
        if s[i].isupper():
            answer += chr( ord('A') + ((ord(s[i]) + n) - ord('A') ) % 26 )
        elif s[i].islower():
            answer += chr( ord('a') + ((ord(s[i]) + n) - ord('a') ) % 26 )
    return answer