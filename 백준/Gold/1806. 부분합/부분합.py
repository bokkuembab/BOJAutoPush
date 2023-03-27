# 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램
# ===>구간합 + 투포인터

# 입력 받기
n, s = map(int, input().split())    # n: 수열의 길이, s: 부분합의 기준(s 이상)
nums = list(map(int, input().split()))    # 수열 리스트

# 초기값 설정
count = []
pref = [0] * (n + 1)    # 누적합 리스트
for i in range(n):
    pref[i + 1] = pref[i] + nums[i]
# print(pref)

left, right = 0, 1
while left < right:
    if right > n:
        break
    
    if pref[right] - pref[left] >= s:
        count.append(right - left)
        left += 1
    else:
        right += 1
    
if count:
    print(min(count))
else:
    print(0)