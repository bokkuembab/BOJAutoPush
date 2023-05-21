import sys
input = sys.stdin.readline

axisX, axisY = map(int, input().split())    # 땅의 가로, 세로의 길이
num_robots, num_commands = map(int, input().split())   # 로봇의 수, 명령의 수

dict_dir = {'E':0, 'N': 1, 'W':2, 'S':3}    # 동북서남
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

robots = [[]]    # 각 로봇의 x, y 좌표, 바라보는 방향 저장
for _ in range(num_robots):
    x, y, direct = input().split()
    robots.append([[int(x) - 1, int(y) - 1], dict_dir[direct]])

commands = [list(input().split()) for _ in range(num_commands)]
for r, com, n in commands:    # 명령 입력 받으며, 충돌 확인
    r, n = int(r), int(n)
    
    if com == 'L':    # 왼쪽으로 90도 회전
        robots[r][1] = (robots[r][1] + n) % 4
    elif com == 'R':    # 오른쪽으로 90도 회전
        robots[r][1] = (robots[r][1] + 3 * n) % 4
    else:    # 바라보는 방향으로 전진
        for _ in range(n):
            
            for i, (now, move) in enumerate(zip(robots[r][0], directions[robots[r][1]])):
                robots[r][0][i] = now + move
            for id, rr in enumerate(robots):    
                if id != r:
                    if robots[r][0] in rr:    # 로봇이 다른 로봇과 충돌했다면, 종료
                        print(f'Robot {r} crashes into robot {id}')
                        exit(0)  
                if not(0 <= robots[r][0][0] < axisX) or not(0 <= robots[r][0][1] < axisY):    # 로봇이 벽에 부딪치면, 종료
                    print(f'Robot {r} crashes into the wall')
                    exit(0)

print('OK')