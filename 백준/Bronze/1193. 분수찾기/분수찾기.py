num = int(input())

for i in range(1, 100000):      # 어느 그룹에 속하는 수인지 확인
    if num <= i*(i+1) / 2:
        break
step = int(num - i*(i-1) / 2)        # 그룹 내의 몇번째 수인지 확인

if i % 2 == 1:           # 짝수번째 수이면
    print('{0}/{1}'.format(i-(step-1), step))
else:                       # 홀수번째 수이면
    print('{0}/{1}'.format(step, i-(step-1)))