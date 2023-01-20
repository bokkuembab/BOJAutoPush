# N*M: 행렬의 크기, A: 첫번째 행렬, B: 두번째 행렬
N, M = map(int, input().split())
A, B = [], []

for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))

for r in range(N):
    for c in range(M):
        print(A[r][c] + B[r][c], end=' ')
    print()