# 좌표 압축: 매우 광범위한 좌표 범위를 줄이기 위해 좌표값이 아닌 좌표들 간의 대소 관계를 저장함
# (해당 좌표의 숫자보다 작은 수의 개수 구하면 됨)

import sys
input = sys.stdin.readline

vec_num = int(input())    # 좌표 수 입력: vec_num
vec_li = list(map(int, input().split()))    # 좌표들 입력: vec_li (리스트 형식)
vec_zip = dict()  # 좌표 압축 딕셔너리 (빠른 탐색을 위해 딕셔너리 형태로 저장)

# set 자료형에 넣어 중복 없애고, 순서대로 정렬
for i, z in enumerate(sorted(set(vec_li))) :
    vec_zip[z] = i
for v in vec_li:
    print(vec_zip[v], end=' ')  # 출력
