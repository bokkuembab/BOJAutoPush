def solution(num_list):
    ans = 1
    for n in num_list: ans *= n
    return 1 if ans < sum(num_list) ** 2 else 0