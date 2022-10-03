# 배열의 길이, 배열 A, B 입력 받기
l = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 배열 a와 b의 요소 곱하기
res = 0     # 결과값 저장
for i in range(l):
    res += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

# 결과 출력
print(res)