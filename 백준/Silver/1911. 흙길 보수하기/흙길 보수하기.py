import sys
input = sys.stdin.readline

# 입력 받기
# n: 웅덩이의 수, l: 널빤지의 크기
n, l = map(int, input().split())
# 웅덩이의 위치 정보 입력 받기
pool = [list(map(int, input().split())) for _ in range(n)]

# 웅덩이 정렬
pool.sort()

# 널빤지의 개수, 웅덩이를 덮은 널빤지의 마지막 위치 
res, s = 0, 0
for srt, end in pool:
  s = max(srt, s)    # 마지막 웅덩이의 위치 고려해주기
  diff = end - s    # 웅덩이의 너비
  count = (diff + l - 1) // l    # 필요한 널빤지의 수
  res += count
  s += count * l

print(res)