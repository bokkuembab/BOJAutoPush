import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)    # 재귀 제한 풀기

n, e, srt = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n + 1)    # 방문 리스트
cnt = 1    # 방문 순서

# node: 현재 방문 노드
def dfs(node):
    global cnt

    # 방문 처리
    visited[node] = cnt
    cnt += 1
    # 오름차순 정렬 후, 방문
    graph[node].sort()
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

dfs(srt)
for i in visited[1:]:
    print(i)