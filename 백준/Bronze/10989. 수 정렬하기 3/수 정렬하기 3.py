# 입력 받는 시간을 줄이기 위한 모듈
import sys

# n: 수의 개수, nlist: 입력받는 수 리스트
n = int(sys.stdin.readline())

# 정렬 시간을 줄이기 위해 배열에 해당 인덱스의 값의 수를 입력함
nlist = [0] * 10001    # 입력 받을 수 있는 최대의 수만큼 배열 생성
for _ in range(n):
    nlist[int(sys.stdin.readline())] += 1

# 출력
for i in range(10001):
    if nlist[i] != 0:
        for _ in range(nlist[i]):
            print(i)