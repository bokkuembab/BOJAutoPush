def solution(num_list):
    s = '+' if len(num_list) >= 11 else '*'
    return eval(s.join([str(n) for n in num_list]))