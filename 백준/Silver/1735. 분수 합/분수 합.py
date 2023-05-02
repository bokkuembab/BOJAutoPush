# 최대공약수 함수
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

c1, p1 = map(int, input().split())  # 첫 번째 분수
c2, p2 = map(int, input().split())  # 두 번째 분수

c = c1 * p2 + c2 * p1   # 분자 계산
p = p1 * p2   # 분모 계산

print(c // gcd(c, p), p // gcd(c, p))