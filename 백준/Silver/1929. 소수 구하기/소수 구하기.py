def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return -1
    return 1

start, end = map(int, input().split())

if start == 1:
    start += 1
for num in range(start, end+1):
    if isPrime(num) > 0:
        print(num)