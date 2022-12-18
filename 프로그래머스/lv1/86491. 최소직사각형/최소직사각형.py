def solution(sizes):
    row, col = 0, 0
    
    for a, b in sizes:
        if a > b:
            a, b = b, a
        row, col = max(row, a), max(col, b)

    return row * col