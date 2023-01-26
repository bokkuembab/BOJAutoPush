# total_paper: 전체 흰색 도화지의 2차원 배열 (0: 흰색, 1: 검은색), num_paper: 색종이의 수
# x, y: 색종이의 왼쪽 아래 꼭짓점 좌표 (모든 색종이의 크기는 10 X 10)
# total_paper = [[0] * 100 for _ in range(100)]
num_paper = int(input())
total_paper = [[0] * 100 for _ in range(100)]
ans = 0

# 색종이 붙이기
for _ in range(num_paper):
    x, y = map(int, input().split())
    for r in range(y, y+10):
        for c in range(x, x+10):
            total_paper[r][c] = 1

# 색종이 붙인 영역의 녋이 구하기
for i in range(100):
    ans += sum(total_paper[i])
print(ans)