# nlist: 입력된 숫자를 저장할 리스트
nlist = list()

for _ in range(5):
    nlist.append(int(input()))

nlist = sorted(nlist)
print(sum(nlist) // len(nlist))    # 평균
print(nlist[len(nlist) // 2])    # 중앙값