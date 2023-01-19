def solution(s):
    ans = []
    
    for ch in s:
        if ans:
            if ans[-1] == ch:
                ans.pop()
            else:
                ans.append(ch)
        else:
            ans.append(ch)

    return 1 if len(ans) == 0 else 0