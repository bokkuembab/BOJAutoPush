import sys
input = sys.stdin.readline

n = int(input())    # 정수 삼각형의 크기
triangle = [list(map(int, input().split())) for _ in range(n)]    # 정수 삼각형의 정보
dp = []    # 해당 위치의 최대 합
for i in range(1, n + 1):
    dp.append([0] * i)
dp[0] = triangle[0]    # 시작 위치 초기화
    
# 순차적으로 탐색
for r in range(1, n):    # (2 ~ n) 탐색
    for c in range(r + 1):
        if c == 0:    # 왼쪽 변의 값이라면,
            dp[r][c] = triangle[r][c] + dp[r - 1][c]    # 바로 위의 값
        elif c == r:    # 오른쪽 변의 값이라면,
            dp[r][c] = triangle[r][c] + dp[r - 1][c - 1]    # 바로 위의 값
        else:     # 중앙의 값이라면,
            dp[r][c] = triangle[r][c] + max(dp[r - 1][c - 1:c + 1])    # (r - 1)의 (c - 1, c) 탐색
            
print(max(dp[n - 1]))
            