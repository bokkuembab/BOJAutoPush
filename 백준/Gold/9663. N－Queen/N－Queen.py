# queen은 상, 하, 좌, 우, 대각선으로 무제한 이동 가능
n = int(input())
row = [-1] * n    # 체스판
ans = 0    # 정답 경우의 수

# 대각선 방향의 queen 확인
def check_cross(cnt):
    # 이전에 놓은 값들만 확인하면 됨
    for i in range(cnt):
        # 0. 각 행에 차례대로 놓고 있으므로 -> 같은 행에 queen 있는지 확인 X
        # 1. 같은 열에 queen 있는지 확인
        if row[cnt] == row[i]: 
            return False
        # 2. 좌상향: [-1, -1]로 움직임 -> row[cnt] - row[i] == cnt - i
        # 3. 우상향: [-1, 1]로 움직임 -> -(row[cnt] - row[i]) == cnt - i
        if abs(row[cnt] - row[i]) == cnt - i:
            return False
    return True
    
# queen은 각 행에 무조건 하나씩만 놓을 수 있음 
# -> 각 행에 차례대로 queen 놓기
def n_queens(cnt):
    global ans

    if cnt == n:
        ans += 1
        return
    
    for c in range(n):
        row[cnt] = c    # [cnt, c] 에 queen을 놓았을 때, 
        if check_cross(cnt):    # 우상향, 좌상향에 queen이 없다면,
            n_queens(cnt + 1)    # 다음 행에 queen 놓기

# 첫 번째 행부터 queen 놓음
n_queens(0)
print(ans)