import sys
input = sys.stdin.readline

n = int(input())    # 사람 수
s = list(list(map(int, input().split())) for _ in range(n))    # 능력치 리스트

visited = [False for _ in range(n)]    # 방문리스트(start 팀)
res = 1e9    # 능력치 차이를 최대로 초기화

# 하나의 팀을 완성하는 함수
def backtracking(depth, idx):
    global res
    if depth == n // 2:    # 팀 구성 완료했다면,
        # 능력치 차이 계산하기
        srt, link = 0, 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:    # start 팀
                    srt += (s[i][j] + s[j][i])
                elif not visited[i] and not visited[j]:    # link팀
                    link += (s[i][j] + s[j][i])

        res = min(res, abs(srt - link))    # 더 작은 값으로 갱신
        return
    
    # 팀 구성중이라면,
    for i in range(idx, n):
        if not visited[i]:    # 아직 팀에 포함되지 않았다면,
            # i가 무조건 팀에 포함되는 경우를 모두 확인한 후, 방문 여부 되돌림
            visited[i] = True
            backtracking(depth + 1, i + 1)
            visited[i] = False

backtracking(0, 0)
print(res)