def solution(n):
    n3 = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        n3 += str(mod)
    
    n3 = n3[::-1]
    
    return sum((3 ** i) * int(n3[i]) for i in range(len(n3)))