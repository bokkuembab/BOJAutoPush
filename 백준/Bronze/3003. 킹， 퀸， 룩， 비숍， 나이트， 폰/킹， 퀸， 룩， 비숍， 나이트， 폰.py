# 각 흰색 피스의 개수 입력 받기
arr = list(map(int, input().split()))

# 세트구성의 각 피스들 개수
ans = [1, 1, 2, 2, 2, 8]

# 세트 구성 개수에서 현재 개수 빼주기
for i in range(len(ans)):
    print(ans[i] - arr[i], end=' ')