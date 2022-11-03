def solution(name):
    answer = 0
    gap = ord('Z') - ord('A') + 1
    min_dist = len(name) - 1
    
    for i, c in enumerate(name):
        a = ord(c) - ord('A')
        b = ord('A') - ord(c) + gap
        answer += min(a, b)
        
        if c == 'A':
            left = i - 1 if i > 0 else i
            right = left + 1 if left < len(name) - 1 else left
            for k in range(right, len(name)):
                if name[k] == 'A':
                    right = k
                else:
                    break

            start_left = left * 2 + (len(name) - 1 - right - 1) + 1
            start_right = left + (len(name) - 1 - right - 1) * 2 + 2
        
            min_dist = min(min_dist, start_left, start_right)
    
    
    return answer + min_dist