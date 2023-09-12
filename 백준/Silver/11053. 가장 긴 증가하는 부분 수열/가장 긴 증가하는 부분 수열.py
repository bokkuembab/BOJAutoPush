import sys
input = sys.stdin.readline

n = int(input())    # 수열의 길이
nlist = list(map(int, input().split()))    # 수열
ans = [1] * n    # 가장 긴 수열의 길이

for i in range(1, n):
    for j in range(i):
        if nlist[j] < nlist[i]:    # 자신보다 작은 수 모두 구함
            ans[i] = max(ans[i], ans[j] + 1)

print(max(ans))