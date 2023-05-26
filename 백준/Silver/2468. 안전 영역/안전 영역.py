
from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
res = 0

def is_safe(row, col, visited, height):
    # 큐 선언
    q = deque([(row, col)])
    visited[row][col] = True    # 방문처리
    
    while q:
        r, c = q.pop()
        for mover, movec in move:
            mr = r + mover
            mc = c + movec
            
            if (0 <= mr < n) and (0 <= mc < n):
                if not visited[mr][mc] and cities[mr][mc] > height:
                    visited[mr][mc] = True
                    q.append((mr, mc))

for i in range(max(map(max, cities))):    # 비의 양이 높이 1보다 작을 수 있으므로 포함해주기
    visited = [[False] * n for _ in range(n)]
    now = 0
    
    for r in range(n):
        for c in range(n):
            if cities[r][c] > i and not visited[r][c]:
                now += 1
                is_safe(r, c, visited, i)
    res = max(res, now)
                
print(res)