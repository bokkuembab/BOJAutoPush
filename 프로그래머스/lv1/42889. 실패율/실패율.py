from collections import Counter

def solution(N, stages):
    
    ans = []
    rest = len(stages)
    fail = []
    trying = [0] * (N + 2)
    
    for s in stages:
        trying[s] += 1
    
    for i in range(1, N + 1):
        if rest != 0:
            fail.append((i, trying[i] / rest))
            rest -= trying[i]
        else:
            fail.append((i, 0))
            
    for item in sorted(fail, reverse=True, key=lambda k: k[1]):
        ans.append(item[0])
    
    return ans