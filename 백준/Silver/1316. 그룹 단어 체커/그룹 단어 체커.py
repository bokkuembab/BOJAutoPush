def checkGroup(str):
    for i in range(0, len(str)-1):
        if str[i] != str[i+1]:
            if str[i+1:].find(str[i]) > -1:
                return -1
    return 1

N = int(input())
num = 0

for _ in range(N):
    str = input()
    if checkGroup(str) > 0:
        num += 1

print(num)