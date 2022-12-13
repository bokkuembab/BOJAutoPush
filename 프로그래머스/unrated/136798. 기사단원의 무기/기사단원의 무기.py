def solution(number, limit, power):
    answer = 0
    arr = [1] * (number + 1)
    arr[0] = 0
    
    for i in range(2, number + 1):
        for j in range(i, number + 1, i):
            arr[j] += 1
    
    for i in range(1, number + 1):
        if arr[i] > limit:
            arr[i] = power
    
    answer = sum(arr)
    
    return answer