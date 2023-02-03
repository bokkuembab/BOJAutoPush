def solution(lottos, win_nums):
    score = [6, 6, 5, 4, 3, 2, 1]
    
    # 우선 확실하게 맞는 번호, 0의 개수 찾기
    match, cnt0 = 0, 0
    
    for l in lottos:
        if l == 0:  
            cnt0 += 1
        if l in win_nums:   
            match += 1

    return score[match + cnt0], score[match]