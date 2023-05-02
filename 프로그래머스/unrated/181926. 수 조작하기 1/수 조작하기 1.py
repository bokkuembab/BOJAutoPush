def solution(n, control):
    key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum([key[k] for k in control])