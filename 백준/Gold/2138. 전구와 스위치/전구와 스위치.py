# 처음부터 끝까지, 이전 전구의 상태에 따라 토글
import copy

n = int(input())    # 전구의 수
start = list(input())   # 현재 전구의 상태
target = list(input())    # 목표 전구의 상태


def is_toggle(now, target):
    now = copy.deepcopy(start)
    ans = 0    # 토글 횟수 초기화
    
    # 두번째 스위치부터 마지막까지 토글 여부 확인
    for i in range(1, n):
        
        if now == target:    # 목표 상태 도달하면, 종료
            return ans
        
        if now[i - 1] != target[i - 1]:    # 현재 위치의 왼쪽 스위치가 목표 상태와 같지 않으면,
            for s in range(i - 1, i + 2):    # 자기 자신과 양쪽 스위치 토글하고, 
                if s < n:    # 마지막 스위치를 위한 범위 제한
                    now[s] = '0' if now[s] == '1' else '1'
            ans += 1    # 횟수 1 늘려주기
            
    return ans if now == target else 1e9

# 두번째 스위치부터 누르는 경우
res = is_toggle(start, target)

# 첫번째 스위치를 눌러야 하는 경우
start[0] = '0' if start[0] == '1' else '1'
start[1] = '0' if start[1] == '1' else '1'

res = min(res, is_toggle(start, target) + 1)

if res < 1e9:
    print(res)
else:
    print(-1)