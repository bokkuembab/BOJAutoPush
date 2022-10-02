N = int(input())
lt = list(map(int, input().split()))
M = max(lt)
res = 0

for i in range(N):
    res += lt[i] / M * 100

print(res / N)