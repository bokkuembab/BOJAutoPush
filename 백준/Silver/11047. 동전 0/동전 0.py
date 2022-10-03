# 동전의 종류, 만들 금액 입력 받기
sort, amount = map(int, input().split())

# n가지 화폐 가치 입력받기
mon = []
for _ in range(sort):
    mon.append(int(input()))

# 필요한 동전 개수
coins = 0

# 큰 수부터 지불가능한지 확인
for i in range(sort - 1, -1, -1):
    q = amount // mon[i]    # 현재 금액을 현재 동전 몇 개로 지불가능한지
    if q > 0:
        coins += q  # 지불한 동전 더하기
        amount = amount % mon[i]    # 나머지 금액 저장

# 총 필요한 동전 개수 출력
print(coins)