import sys
from collections import Counter

# 수의 개수, 각 수들 입력 받기
n = int(sys.stdin.readline())
arr = []
id = [0] * 8001
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 산술 평균 (소수점 첫째자리에서 반올림)
print(int(round(sum(arr) / n, 0))) 

# 중앙값
arr.sort()  # 정렬 수행
print(arr[n // 2])   

# 최빈값
c = Counter(arr)
# 최빈값이 여러개면 두번째로 작은 값 출력
if len(c) > 1 and c.most_common()[0][1] == c.most_common()[1][1]:
    print(c.most_common()[1][0])
else:
    print(c.most_common()[0][0])

# 범위
print(max(arr) - min(arr))    