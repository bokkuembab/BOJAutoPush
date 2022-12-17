def solution(price, money, count):

    return max(0, sum(price * c for c in range(1, count + 1)) - money)