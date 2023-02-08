# 입력 받는 시간을 줄이기 위한 모듈
import sys

# n: 수의 개수, nlist: 입력받는 수 리스트
n = int(sys.stdin.readline())
nlist = list()

for _ in range(n):
    nlist.append(int(sys.stdin.readline()))

# 오름차순 정렬: sort
nlist.sort()

# 출력
for i in nlist:
    print(i)