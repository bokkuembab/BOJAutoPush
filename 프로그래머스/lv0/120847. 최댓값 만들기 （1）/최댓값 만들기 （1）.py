def solution(numbers):
    ans = sorted(numbers)[-2:]
    return ans[0] * ans[1]