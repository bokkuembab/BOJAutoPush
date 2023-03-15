from collections import deque

# col: 상자의 가로 칸 수, row: 세로 칸 수
# 2 <= col, row <= 1,000
col, row = map(int, input().split())

# 토마토 정보 입력받기
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
box = []
for _ in range(row):
    box.append(list(map(int, input().split())))

# 이동 가능한 경우의 수 (상, 하, 좌, 우)
mrow = [-1, 1, 0, 0]
mcol = [0, 0, -1, 1]

q = deque([])    # 큐 선언
for r in range(row):    # 익은 토마토 위치 큐에 넣어주기
    for c in range(col):
        if box[r][c] > 0:
            q.append((r, c, 0))

while q:
    # 큐에서 값 꺼내기
    r, c, cnt = q.popleft()
    
    # 이동가능한 구간 모두 확인
    for mr, mc in zip(mrow, mcol):
        # 이동
        mvr = r + mr
        mvc = c + mc
        
        # 인덱스가 범위 안에 있고, 값이 0이라면 -> box에 익은거 표시, 큐에 추가, cnt + 1 
        if (0 <= mvr < row) and (0 <= mvc < col) and not box[mvr][mvc]:
            box[mvr][mvc] = 1
            q.append((mvr, mvc, cnt + 1))

# 토마토가 모두 익지는 못하는 상황이면, -1을 출력
for r in range(row):
    for c in range(col):
        if not box[r][c]:
            cnt = -1
            
# 정답 출력
print(cnt)