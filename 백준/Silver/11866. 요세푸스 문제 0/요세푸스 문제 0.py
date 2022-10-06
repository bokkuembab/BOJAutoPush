# 인원 수, 제거할 순서 입력 받기
n, k = map(int, input().split())

# 1부터 n까지의 숫자 갖는 리스트 생성
arr = []
for i in range(1, n + 1):
    arr.append(i)

# 현재 가리키고 있는 인덱스
id = 0

# 요세푸스 순열 출력
print('<', end='')
for i in range(n):
    id = (id + k - 1)  % (n - i)
    print(arr[id], end='')
    del arr[id]
    if arr:
        print(', ', end='')
print(">")