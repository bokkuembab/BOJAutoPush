def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        if not n % 2 : answer[0] += 1
        else: answer[1] += 1
    return answer