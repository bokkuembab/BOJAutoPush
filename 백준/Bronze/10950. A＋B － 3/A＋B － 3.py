N = int(input())
l=[]

for i in range(N):
    a, b = map(int, input().split())
    l.append(a+b)

for i in range(N):
    print(l[i])