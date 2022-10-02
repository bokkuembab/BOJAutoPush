lt = list(range(1,10001))
lt_r = []

for n in lt:
    sum = n
    while n > 0:
        sum += n % 10
        n //= 10
    lt_r.append(sum)

for c in lt:
    if c not in lt_r:
        print(c)