# 톱니바퀴 정보 (0: N극, 1: S극)
n = 4    # 톱니바퀴의 수
wheels = list(list(map(int, input())) for _ in range(n))
k = int(input())    # 회전 횟수
# 회전 방법 (번호, 방향) - (1: 시계 방향, -1: 반시계 방향)
rotations = list((map(int, input().split())) for _ in range(k))   

# 지정한 방향으로 해당 바퀴를 회전시켜 반환하는 함수
def rotate_wheel(idx, rotate):

    if rotate < 0:    # 반시계 방향 회전
        return wheels[idx][1:] + [wheels[idx][0]]
    else:    # 시계 방향 회전
        return [wheels[idx][-1]] + wheels[idx][:-1]
    
# 양쪽 톱니바퀴가 다른지 확인하는 함수
def check_diff(now, nxt):
    
    if now < nxt:    # 이웃 톱니바퀴가 오른쪽에 위치
        if wheels[now][2] == wheels[nxt][6]:
            return False
        return True
    else:    # 이웃 톱니바퀴가 왼쪽에 위치
        if wheels[now][6] == wheels[nxt][2]:
            return False
        return True
        
for now, dir in rotations:
    now -= 1
    new_rot = [(now, dir)]    # 회전시킬 정보 저장 리스트

    for d in [-1, 1]:    # 왼쪽, 오른쪽 확인
        nxt, nxt_dir = now + d, -dir

        while nxt >= 0 and nxt < n:
            if check_diff(nxt - d, nxt):
                new_rot.append((nxt, nxt_dir))
                nxt += d
                nxt_dir *= -1
            else:
                break

    # 회전시키기
    for wh, dir in new_rot:
        wheels[wh] = rotate_wheel(wh, dir)

# 점수 계산
score = 0
for i in range(n):
    score += wheels[i][0] * (2 ** i)

print(score)