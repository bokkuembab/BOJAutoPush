from collections import defaultdict
import sys
input = sys.stdin.readline

x_num, y_num = map(int, input().split())    # 도시의 가로, 세로 크기
k = int(input())    # 공사중인 도로의 수
roads = defaultdict(list)    # 공사중 도로 정보
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    (x1, x2) = (x1, x2) if x1 < x2 else (x2, x1)
    (y1, y2) = (y1, y2) if y1 < y2 else (y2, y1)
    if (x1, y1) not in roads[(x2, y2)]:
        roads[(x2, y2)].append((x1, y1))

dp = [[0] * (y_num + 1) for _ in range(x_num + 1)]    # 해당 위치에 도달하는 경우의 수

# dp 초기화 (양 끝의 경우의 수: 1)
for x in range(1, x_num + 1):
    if (x, 0) in roads: break
    dp[x][0] = 1
for y in range(1, y_num + 1):
    if (0, y) in roads: break
    dp[0][y] = 1

# dp 채우기
for x in range(1, x_num + 1):
    for y in range(1, y_num + 1):
        dp[x][y] = dp[x-1][y] + dp[x][y-1]
        
        for dx, dy in roads[(x, y)]:
            dp[x][y] -= dp[dx][dy]

print(dp[-1][-1])