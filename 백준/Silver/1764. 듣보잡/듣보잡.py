import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nset = set()
for _ in range(n):
    nset.add(input().rstrip())
    
mset = set()
for _ in range(m):
    mset.add(input().rstrip())
    
nmset = nset & mset
nmset = sorted(nmset)
print(len(nmset))
for e in nmset:
    print(e)