N = int(input())
num = 0

for i in range(1,N+1):
    if i < 100:
        num += 1
    elif i == 1000:
        continue
    else:
        k = (i // 10) % 10
        if (i // 100 - k) == (k - i % 10):
            num += 1

print(num)