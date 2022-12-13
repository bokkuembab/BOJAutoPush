def solution(k, score):
    answer = []
    prize = []
    
    for s in score:
        
        prize.append(s)
        
        if len(prize) > k:
            prize.remove(min(prize))
            
        answer.append(min(prize))
    
    return answer