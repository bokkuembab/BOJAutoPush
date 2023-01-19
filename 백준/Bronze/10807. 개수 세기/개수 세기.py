# n: 정수의 개수, li: 정수 리스트, v: 찾으려는 정수
n = int(input())
li = list(map(int, input().split()))
v = int(input())

print(li.count(v))