def solution(d, budget):
    ans = 0
    d.sort()
    
    for n in d:
        budget -= n
        if budget < 0:
            break
        ans += 1
        
    return ans