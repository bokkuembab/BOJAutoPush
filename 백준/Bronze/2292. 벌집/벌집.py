room = int(input())

for i in range(100000):
    if room - 1 <= 3 * i * (i + 1):     # 둘러싼 육각형은 바깥으로 갈수록 6*i 만큼의 개수를 가짐
        print(i + 1)
        break