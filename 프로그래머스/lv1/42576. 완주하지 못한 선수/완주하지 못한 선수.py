from collections import Counter

def solution(participant, completion):
    
    ans = Counter(participant) - Counter(completion)
    ans = list(ans.keys())[0]
    
    return ans