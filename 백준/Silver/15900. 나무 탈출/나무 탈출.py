import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

n = int(input())    # 트리 정점의 수
tree = [[] for _ in range(n + 1)]    # 간선 정보
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
dist = [0] * (n + 1)    # 각 노드에서 루트노드까지의 거리
visited = [False] * (n + 1)    # 방문 여부 리스트

def dfs(node):
    visited[node] = True
    for nxt in tree[node]:
        if not visited[nxt]:
            dist[nxt] = dist[node] + 1
            dfs(nxt)

# 1부터 방문
dfs(1)

# 리프 노드의 경우에만 거리 더해줌
ans = 0    # 말을 움직일 수 있는 총 수
for i in range(2, n + 1):
    if len(tree[i]) == 1: ans += dist[i]

print('Yes' if ans % 2 else 'No')