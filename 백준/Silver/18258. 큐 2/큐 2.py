import sys
input = sys.stdin.readline

# 큐 생성
queue = []    # 큐
now = 0    # 현재 가리키고 있는 인덱스

n = int(input())    # 명령의 수
for _ in range(n):

    # 명령어 저장하기
    tmp = input().split()
    if len(tmp) < 2:
        cmd = tmp[0]
    else:
        cmd, num = tmp[0], int(tmp[1])

    # 명령어 수행 시작
    # push X: 정수 X를 큐에 넣는 연산이다.
    if cmd == "push":
        queue.append(num)

    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif cmd == "pop":
        if now < len(queue):    # 큐에 정수가 있다면,
            print(queue[now])
            now += 1
        else:    # 큐에 정수가 없다면,
            print(-1)

    # size: 큐에 들어있는 정수의 개수를 출력한다.
    elif cmd == "size":
        print(len(queue) - now)

    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif cmd == "empty":
        if now >= len(queue):
            print(1)
        else:
            print(0)

    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif cmd == "front":
        if now < len(queue):    # 큐에 정수가 있다면,
            print(queue[now])
        else:    # 큐에 정수가 없다면,
            print(-1)

    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif cmd == "back":
        if now < len(queue):    # 큐에 정수가 있다면,
            print(queue[-1])
        else:    # 큐에 정수가 없다면,
            print(-1)