def solution(arr1, arr2):
    # arr1(n*m) * arr2(m*k) 이므로 결과는 n * k
    row, col, mm = len(arr1), len(arr2[0]), len(arr2)
    ans = [[0] * col for _ in range(row)]
    
    for r in range(row):
        for c in range(col):
            for m in range(mm):
                ans[r][c] += arr1[r][m] * arr2[m][c]
    return ans