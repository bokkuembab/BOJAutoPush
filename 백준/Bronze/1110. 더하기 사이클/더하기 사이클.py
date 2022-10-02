N = int(input())

temp = N
i = 0

while True:
    i += 1
    temp = (10 * (temp % 10)) + (((temp // 10) + (temp % 10)) % 10)
    if N == temp:
        break

print(i)