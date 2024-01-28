import sys

# 빈 칸에 1~9 숫자 넣을 수 있는지 확인하는 함수
def checkRow(r, n):    # 가로
    for i in range(9):
        if sdoku[r][i] == n:
            return False
    return True
def checkCol(c, n):    # 세로
    for i in range(9):
        if sdoku[i][c] == n:
            return False
    return True
def checkBox(r, c, n):    # 3*3 박스
    row = (r // 3) * 3
    col = (c // 3) * 3
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if sdoku[i][j] == n:
                return False
    return True

# 빈 칸 하나씩 채우는 함수
def fill_blanks(idx):

    # 종료 조건
    if idx == len(blank):
        # 결과 출력
        for r in range(9):
            print(*sdoku[r])
        exit(0)
    
    # 1~9까지 넣어봄
    for n in range(1, 10):
        br, bc = blank[idx]
        if checkRow(br, n) and checkCol(bc, n) and checkBox(br, bc, n):
            sdoku[br][bc] = n       
            fill_blanks(idx + 1)
            sdoku[br][bc] = 0

if __name__ == '__main__':

    input = sys.stdin.readline

    sdoku = [list(map(int, input().split())) for _ in range(9)]
    # 빈 칸 저장
    blank = []
    for i in range(9):
        for j in range(9):
            if sdoku[i][j] == 0: 
                blank.append((i, j))

    fill_blanks(0)