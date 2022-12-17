def solution(n, m):
    answer = [1]
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            answer[0] = i
            
    answer.append(n * m // answer[0])
    return answer