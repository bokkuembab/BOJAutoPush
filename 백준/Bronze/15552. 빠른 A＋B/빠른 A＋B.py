import sys      # sys 읽기

n = int(sys.stdin.readline())

for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)