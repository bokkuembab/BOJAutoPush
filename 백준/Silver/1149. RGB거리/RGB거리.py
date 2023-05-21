import sys
input = sys.stdin.readline

n = int(input())    # 집의 수
house = [list(map(int, input().split())) for _ in range(n)]    # 각 집의 R, G, B 비용
for i in range(1, n):
    house[i][0] += min(house[i-1][1], house[i-1][2])    # 현재 R 선택, 이전에 G, B 선택 중 최소
    house[i][1] += min(house[i-1][0], house[i-1][2])    # 현재 G 선택, 이전에 R, B 선택 중 최소
    house[i][2] += min(house[i-1][0], house[i-1][1])    # 현재 B 선택, 이전에 R, G 선택 중 최소

print(min(*house[n-1]))