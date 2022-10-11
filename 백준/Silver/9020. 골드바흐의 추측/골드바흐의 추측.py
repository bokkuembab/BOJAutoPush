def is_prime(n):
    if n == 1:
        return -1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i ==0:
            return -1
    return 1

tnum = int(input())

for _ in range(tnum):
    t = int(input())
    a, b = t // 2, t // 2

    while a > 0:
        if is_prime(a) > 0 and is_prime(b) > 0:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
