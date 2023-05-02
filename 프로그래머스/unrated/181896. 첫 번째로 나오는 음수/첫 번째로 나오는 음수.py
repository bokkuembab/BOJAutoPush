def solution(num_list):
    id = -1
    for i, n in enumerate(num_list):
        if n < 0:
            id = i
            break
    return -1 if id < 0 else id