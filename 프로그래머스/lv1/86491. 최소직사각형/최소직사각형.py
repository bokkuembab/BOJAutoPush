def solution(sizes):
    ans = [0, 0]
    for n in sizes:
        n.sort()
        print('n', n)
        ans = ( max(ans[0], n[0]), max(ans[1], n[1]) )

    return ans[0] * ans[1]