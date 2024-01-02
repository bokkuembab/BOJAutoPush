n, l = map(int, input().split())
visited = [False] * (n + 1)    # 방문리스트
nums = []    # 선택한 숫자들 저장 리스트

def backtracking():

    # 종료 조건
    if len(nums) == l:
        print(' '.join(map(str, nums)))
        return
    
    # 1 ~ n 반복
    for i in range(1, n + 1):
        if not visited[i]:
            
            # 이전값보다 작은 수가 나오면 중복 -> 다음 숫자로 넘어감
            if nums:     
                if i < nums[-1]: continue

            visited[i] = True
            nums.append(i)
            backtracking()
            nums.pop()
            visited[i] = False

backtracking()