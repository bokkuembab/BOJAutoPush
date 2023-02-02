# N : 응시자의 수, k : 상을 받는 사람의 수
# xlist : 입력받은 각 학생의 점수 리스트
N, k = map(int, input().split())
xlist = list(map(int, input().split()))

xlist = sorted(xlist, reverse=True)

print(xlist[k - 1])