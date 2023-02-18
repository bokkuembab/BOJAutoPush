# n: 거스름돈의 액수
import sys
input = sys.stdin.readline

n = int(input())
rst = 0
    
if (n % 5) % 2 == 0:    # 5로 최대로 거슬러 주고, 나머지는 2로 거슬러 줄 수 있다면
    rst = (n // 5) + ((n % 5) // 2)
    n = 0
else:
    for i in range(n // 5 - 1, -1, -1):    # 5로 거슬러 주는 돈을 하나씩 줄임
        if (n - 5 * i) % 2 == 0:      # 5로 거슬러주고, 나머지는 2로 거슬러 줄 수 있다면
            rst = i + ((n - 5 * i) // 2)
            n = 0
            break
        
print(-1 if n else rst)    # 5, 2로 거슬러줄 수 있었는지 확인하고 결과 출력