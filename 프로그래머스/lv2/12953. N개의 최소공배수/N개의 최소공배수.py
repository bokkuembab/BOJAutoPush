# 최대공약수 찾는 재귀 함수: 유클리드 호제법
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def solution(arr):
    lcm = 1
    
    for n in arr:
        g = gcd(lcm, n)
        # 최소공배수: 두 수의 곱 / 최대공약수
        lcm = int(n * lcm / g)
        print(lcm)
        
    return lcm