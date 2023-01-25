# grid: 9*9 격자판 리스트
grid = []
maxn, maxi = 0, [0, 0]
for i in range(9):
    grid.append(list(map(int, input().split())))
    if maxn < max(grid[i]):
        maxn, maxi[0], maxi[1] = max(grid[i]), i, grid[i].index(max(grid[i]))

print(maxn)
print(maxi[0] + 1, maxi[1] + 1)