amount = int(input())

def check(a):
    for i in range(amount // 5, -1, -1):
        if (amount - i*5) % 3 == 0:
            print(i + (amount - i*5) // 3)
            return 1
    return -1

if check(amount) < 0:
    print(-1)
