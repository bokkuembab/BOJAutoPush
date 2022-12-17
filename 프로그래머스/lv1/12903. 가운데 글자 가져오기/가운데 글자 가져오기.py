def solution(s):
    k = len(s) // 2
    return s[k] if len(s) % 2 != 0 else s[k-1: k+1]