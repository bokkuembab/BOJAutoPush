plist = [1] * (123456*2)
plist[0] = 0
plist[1] = 1
for num in range(2,123456*2 + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            plist[num-1] = 0
            break

while True:
    N = int(input())
    if N == 0:
        break
    print(sum(plist[N:2*N]))