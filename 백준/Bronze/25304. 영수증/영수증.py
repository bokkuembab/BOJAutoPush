total = int(input())
n = int(input())
sum = 0

for _ in range(n):
    p, num = map(int, input().split())
    sum += p * num

if sum == total:
    print('Yes')
else:
    print('No')