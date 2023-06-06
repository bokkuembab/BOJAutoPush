import sys
input = sys.stdin.readline

# mlist가 nlist 안에 존재하는지
n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()

for i in mlist:
    left, right = 0, n - 1
    check = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if nlist[mid] == i:
            check = 1
            break
        if nlist[mid] < i:
            left = mid + 1
        else:
            right = mid - 1
            
    print(check)