# N: 수의 개수, nlist: 입력된 수의 리스트
N = int(input())
nlist = []

for _ in range(N):
    nlist.append(int(input()))

# nlist 정렬
nlist = sorted(nlist)

for n in nlist:
    print(n)
