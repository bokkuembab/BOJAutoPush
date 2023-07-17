#  "enter"인 경우는 출근, "leave"인 경우는 퇴근
# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력

n = int(input())
log = dict()
for _ in range(n):
    name, check = input().split()
    if check == "enter":
        log[name] = True
    else:
        log[name] = False
     
log = sorted(log.items(), reverse=True)   
for n, l in log:
    if l:
        print(n)