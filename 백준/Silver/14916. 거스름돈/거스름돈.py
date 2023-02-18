import sys
input = sys.stdin.readline

n = int(input())
values = [5, 2]
rst = 0
    
if (n % 5) % 2 == 0:
    rst = (n // 5) + ((n % 5) // 2)
    n = 0
else:
    for i in range(n // 5, -1, -1):
        if (n - 5 * i) % 2 == 0:
            rst = i + ((n - 5 * i) // 2)
            n = 0
            break
        
print(-1 if n else rst)