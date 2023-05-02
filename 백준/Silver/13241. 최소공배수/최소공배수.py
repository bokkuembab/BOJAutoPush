# 최대공약수 함수
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

n1, n2 = map(int, input().split())
print(n1 // gcd(n1, n2) * n2)   # 최소공배수: 두 수의 곱 / 두 수의 최대 공약수