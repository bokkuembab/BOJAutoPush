from collections import Counter

def solution(babbling):
    cnt = 0
    cando = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        for c in cando:
            if c*2 not in b:
                b = b.replace(c, '-')
        b = b.replace('-', '')
        
        if not b:
            cnt += 1
        
    return cnt