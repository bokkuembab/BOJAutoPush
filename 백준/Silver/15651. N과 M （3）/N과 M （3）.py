n, l = map(int, input().split())
visited = [False] * (n + 1)
nums = []

def backtracking():

    # 종료 조건
    if len(nums) == l:
        print(' '.join(map(str, nums)))
        return
    
    # 1부터 n까지 반복
    for i in range(1, n + 1):
        nums.append(i)
        backtracking()
        nums.pop()

backtracking()
    