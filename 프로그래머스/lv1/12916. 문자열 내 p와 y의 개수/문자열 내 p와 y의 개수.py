def solution(s):
    answer = 0
    
    for chr in s:
        if chr == 'p' or chr == 'P':
            answer += 1
        elif chr == 'y' or chr == 'Y':
            answer -= 1

    return answer == 0