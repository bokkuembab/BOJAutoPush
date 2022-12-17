def solution(n):
    answer = sorted(str(n))
    answer.reverse()

    return int(''.join(answer))