# 1~30 들어있는 리스트 생성 후, 입력을 하나씩 제거하기
students = list(range(1, 31))
for _ in range(28):
    students.remove(int(input()))

for s in students:
    print(s)