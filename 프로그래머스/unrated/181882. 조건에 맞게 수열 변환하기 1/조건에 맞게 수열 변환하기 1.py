def solution(arr):
    answer = []
    
    for n in arr:
        if n >= 50 and not n % 2: answer.append(n / 2)
        elif n < 50 and n % 2: answer.append(n * 2)
        else: answer.append(n)
    
    return answer