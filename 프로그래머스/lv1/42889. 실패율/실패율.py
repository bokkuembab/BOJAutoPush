from collections import Counter

def solution(N, stages):
    
    cnt = dict()
    rest = len(stages)
    
    for i in range(1, N + 1):
        try_men = stages.count(i)
        if rest != 0:
            cnt[i] = try_men / rest
            rest -= try_men
        else:
            cnt[i] = 0
            
    cnt = sorted(cnt, reverse=True, key = lambda k: cnt[k])
    
    return cnt