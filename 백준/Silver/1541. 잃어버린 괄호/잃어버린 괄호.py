# 식 입력받기
formula = input()

# -를 기준으로 나누기
f = formula.split('-')

# - 등장 이전의 + 계산으로 결과값 초기화
res = 0
nlist = f[0].split('+')
for i in nlist:
    res += int(i)

# - 등장 이후의 계산 결과는 전부 빼줌
for i in range(1, len(f)):
    nlist = f[i].split('+')
    sumn = 0
    for j in nlist:
        sumn += int(j)
    res -= sumn

# 연산 결과 출력
print(res)