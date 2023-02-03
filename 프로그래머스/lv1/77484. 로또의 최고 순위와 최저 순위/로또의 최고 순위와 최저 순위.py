def solution(lottos, win_nums):
    answer = []
    score = [6, 6, 5, 4, 3, 2, 1]
    
    # 우선 확실하게 맞는 번호, 0의 개수 찾기
    match, cnt = 0, 0
    
    for l in lottos:
        if l == 0:  
            cnt += 1
        if l in win_nums:   
            match += 1
    
    # 최고, 최저 등수 찾기
    answer.append(score[match + cnt])
    answer.append(score[match])

    return answer