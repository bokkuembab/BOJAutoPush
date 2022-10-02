sP, dP, price = map(int, input().split())

if price - dP <= 0:     # 손익분기점이 없을 경우
    print(-1)
else:
    print(sP // (price - dP) + 1)       # 손익분기점 계산