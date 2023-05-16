n = int(input())    # 시작 숫자
res = [0] * (n + 1)    # 최종 연산 횟수 (해당 인덱스가 1이 되기 위한 최소 연산 횟수 저장)

# bottom-up 방식 (1로 만들기 위한 최소 횟수를 1~n까지 확인)
for i in range(2, n + 1):
    res[i] = res[i - 1] + 1    # 바로 전 값에서 1을 빼는 연산 한 번 수행해서 만들 수 있으므로
    
    if not i % 2:    # 2으로 나누어 떨어지면, 3으로 나눔
        res[i] = min(res[i], res[i // 2] + 1)    # 횟수가 더 작은 값으로 갱신함
        
    if not i % 3:    # 3으로 나누어 떨어지면, 3으로 나눔
        res[i] = min(res[i], res[i // 3] + 1)    # 횟수가 더 작은 값으로 갱신함
        
print(res[n])