def isPrime(n):
    if n == 1:
        return -1
    else:
        for i in range(2, n):
            if n % i == 0:
                return -1
    return 1

N = int(input())
nlist = input().split()
sum = 0

for num in nlist:
    if isPrime(int(num)) > 0:
        sum += 1

print(sum)
