def solution(arr):
    answer = []
    
    for n in arr:
        if [n] == answer[-1:]:
            continue
        answer.append(n)
    
    return answer