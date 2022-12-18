def solution(s, n):
    s = list(s)

    for i in range(len(s)):
        
        if s[i].isupper():
            s[i] = chr( ord('A') + ((ord(s[i]) + n) - ord('A') ) % 26 )
        elif s[i].islower():
            s[i] = chr( ord('a') + ((ord(s[i]) + n) - ord('a') ) % 26 )
            
    return ''.join(s)