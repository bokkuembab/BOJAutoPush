A, B = map(int, input().split())

while(True):
    if A == 0 and B == 0:
        break
    print(A+B)
    A, B = map(int, input().split())
