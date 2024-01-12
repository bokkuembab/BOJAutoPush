import sys
input = sys.stdin.readline

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]    # 능력치 리스트
visited = [False] * n    # start 팀원 여부(True: start 팀, False: link 팀)
res = 1e9     # 최소 점수 차이

# start, link 팀원 점수 계산
def cal_score():
    srt, lnk = 0, 0

    # 0 ~ (n-1) 점수 계산
    # (짝을 짓게 되므로 마지막 한 사람은 이미 매칭된 상태)
    for i in range(n - 1):
        # 다음 사람부터 같은 팀인지 확인
        for j in range(i + 1, n):
            if visited[i] and visited[j]:    # start 팀
                srt += stats[i][j] + stats[j][i]
            elif not visited[i] and not visited[j]:    # link 팀
                lnk += stats[i][j] + stats[j][i]
    return abs(srt - lnk)

# start 팀원 매칭
def match_teams(limit, cnt, now):
    global res

    # 종료 조건
    if cnt == limit:
        res = min(res, cal_score())
        return
    
    # 현재 ~ (n-1) 순회
    # (본인의 다음 사람들을 확인하므로)
    for i in range(now, n):
        if not visited[i]:
            visited[i] = True
            match_teams(limit, cnt + 1, i)
            visited[i] = False

# srt의 팀원 수 1부터 같을 때까지 늘리며 팀 매칭
# (srt팀이 1 ~ n//2 일 때까지 확인했으므로, link 팀도 동시에 확인됨)
for limit in range(1, n // 2 + 1):
    match_teams(limit, 0, 0)
print(res)