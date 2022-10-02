A = int(input())
B = int(input())
C = int(input())
N = A * B * C
lt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while N > 0:
    lt[N % 10] += 1
    N = N // 10

for i in range(10):
    print(lt[i])