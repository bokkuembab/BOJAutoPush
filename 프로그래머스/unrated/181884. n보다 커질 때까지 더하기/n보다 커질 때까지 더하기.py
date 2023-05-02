def solution(numbers, n):
    ans = 0
    for i in numbers:
        if ans > n: break
        ans += i
    return ans