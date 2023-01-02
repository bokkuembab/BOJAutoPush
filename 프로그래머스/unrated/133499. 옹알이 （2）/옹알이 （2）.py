def solution(babbling):
    cnt = 0
    
    for b in babbling:
        for c in ['aya', 'ye', 'woo', 'ma']:
            if c*2 not in b:
                b = b.replace(c, ' ')        
                
        if len(b.strip()) == 0:
            cnt += 1
        
    return cnt