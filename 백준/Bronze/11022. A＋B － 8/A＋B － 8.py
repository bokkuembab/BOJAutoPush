n = int(input())

for i in range(1, n+1):
    A, B = map(int, input().split())
    print("Case #{0}: {1} + {2} = {3}".format(i, A, B, A+B))