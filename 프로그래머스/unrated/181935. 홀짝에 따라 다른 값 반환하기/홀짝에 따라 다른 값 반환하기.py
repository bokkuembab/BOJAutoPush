def solution(n):
    answer = 0
    if not n % 2:
        answer = sum([n ** 2 if not n % 2 else 0 for n in range(1, n + 1)])
    else:
        answer = sum([n if n % 2 else 0 for n in range(1, n + 1)])
    return answer