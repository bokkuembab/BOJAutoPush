def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def solution(arr):
    lcm = 1
    
    for n in arr:
        g = gcd(lcm, n)
        lcm = int(n * lcm / g)
        
    return lcm