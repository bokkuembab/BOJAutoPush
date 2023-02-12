# dot_n: 점의 개수, dots: 점들을 저장하는 리스트

dot_n = int(input())
dots = []

for _ in range(dot_n):
    dots.append(tuple(map(int, input().split())))   # 점 하나씩 튜플 형태로 입력받아 리스트에 넣기

dots.sort()    # x, y 좌표 순서대로 정렬
for x, y in dots:
    print(x, y)   # 출력