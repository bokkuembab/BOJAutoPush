def solution(d, budget):
    ans = 0
    d.sort()
    
    for i in range(len(d)):
        budget -= d[i]
        if budget >= 0:
            ans += 1
        
    return ans