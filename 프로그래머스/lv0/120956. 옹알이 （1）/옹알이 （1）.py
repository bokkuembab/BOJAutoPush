def solution(babbling):
    answer = 0
    cando = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        for c in cando:
            b = b.replace(c, '-')
        b = b.replace('-', '')
        
        if not b:
            answer += 1
    
    return answer