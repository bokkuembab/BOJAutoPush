# 인원수, 인출 시간 입력 받기
num = int(input())
dtime = list(map(int, input().split()))

# 인출 시간 적은 순으로 정렬
dtime.sort()

# 각 사람이 인출하는 데 걸리는 시간 구하기
for i in range(1, num):
    dtime[i] += dtime[i - 1]

# 결과 출력
print(sum(dtime))