row = int(input())    # 세로의 길이
dp = [0] * 100000    # dp 리스트
dp[0], dp[1] = 3, 7

if row > 1:
    for i in range(2, row):
        dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901

print(dp[row-1])