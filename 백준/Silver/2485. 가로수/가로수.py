# 나무들의 간격을 우선 계산함
# 나무들의 간격의 최대공약수만큼의 거리에 나무가 없으면, 나무를 심어야 함

import sys
input = sys.stdin.readline

n = int(input())    # 현재 심은 나무의 개수
dist_trees = []    # 나무들 사이의 거리
before = int(input())    # 이전 나무의 위치
for _ in range(n - 1):
    tmp = int(input())
    dist_trees.append(tmp - before)
    before = tmp

# 최대공약수 함수 (유클리드호제법)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# 나무들의 간격의 최대공약수 구하기
gcd_trees = dist_trees[0]
for i in range(1, len(dist_trees)):
    gcd_trees = gcd(gcd_trees, dist_trees[i])

# 최대공약수보다 넓은 간격을 가지면 (간격 // 최대공약수 - 1)만큼 나무 심어주기
res = 0    # 추가로 심을 나무의 수
for d in dist_trees:
    if d > gcd_trees:
        res += d // gcd_trees - 1

print(res)