def solution(num_list):
    
    c1 = eval('*'.join([str(n) for n in  num_list]))
    c2 = sum(num_list) ** 2
    
    if c1 < c2: return 1

    return 0