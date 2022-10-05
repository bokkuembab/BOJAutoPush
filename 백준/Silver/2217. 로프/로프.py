# 로프의 개수, 각 로프의 중량 입력 받기
n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

w = 0       # 최대 중량 0으로 초기화
num = n     # 사용된 로프의 수를 최대값으로 초기화

# 각 로프의 중량 작은 순서대로 정렬
ropes.sort()

# 모두 사용하며 최대 중량 확인
for i in range(n):
    w = max(ropes[i] * num, w)
    num -= 1

# 계산한 최대 중량 결과 출력
print(w)