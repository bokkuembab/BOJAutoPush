def solution(participant, completion):
    check = {}
    
    for p in participant:
        if p not in check:
            check[p] = 1
        else:
            check[p] += 1
        
    for c in completion:
        check[c] -= 1
            
    for p in check:
        if check[p] != 0:
            print(check[p])
            return p