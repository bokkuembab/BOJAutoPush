def solution(babbling):
    answer = 0
    
    for b in babbling:
        b = b.replace('aya', '-').replace('ye', '-').replace('woo', '-').replace('ma', '-').replace('-', '')
        if not b:
            answer += 1
    
    return answer