from collections import Counter

def solution(s):
    ans = []
    s = list(s)
    
    while s:
        tmp = s.pop()
        if ans:
            if ans[-1] == tmp:
                ans.pop()
            else:
                ans.append(tmp)
        else:
            ans.append(tmp)

    return 1 if len(ans) == 0 else 0