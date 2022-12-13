def solution(k, score):
    answer = []
    prize = []
    
    for s in score:
        if len(prize) < k:
            prize.append(s)
            answer.append(min(prize))
            continue
            
        if min(prize) < s:
            prize.remove(min(prize))
            prize.append(s)
            answer.append(min(prize))
            continue
            
        answer.append(min(prize))
    
    return answer