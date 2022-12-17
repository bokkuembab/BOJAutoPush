def solution(price, money, count):
    answer = money - sum(price * c for c in range(1, count + 1))

    return 0 if answer >= 0 else -answer