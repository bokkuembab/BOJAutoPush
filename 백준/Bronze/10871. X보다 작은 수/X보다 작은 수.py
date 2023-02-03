# N: 수열의 길이, A: 수열 리스트, X: 기준값

N, X = map(int, input().split())
data = list(map(int, input().split()))

for n in data:
    if n < X:
        print(n, end=' ')