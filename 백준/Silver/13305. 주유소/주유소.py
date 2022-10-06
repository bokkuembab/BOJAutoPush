# 도시의 수 n, 도로의 길이 road, 각 도시의 주유 가격 oil 입력 받기
n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

# 최소 주유 가격을 출발 시 필요한 주유비로 초기화
price = oil[0] * road[0]
mp = oil[0]     # 현재까지 중 최소 주유비 초기화

# 이전까지의 주유비 중 최소 선택해서 주유
for i in range(1, n - 1):
    mp = min(mp, oil[i])       # 현재까지 중 최소 주유비 계산
    price += mp * road[i]

# 계산한 최소 주유 금액 출력
print(price)