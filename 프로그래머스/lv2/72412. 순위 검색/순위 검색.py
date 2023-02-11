# info: 지원자의 4가지 정보, 획득 코딩테스트 점수 (스페이스로 구분)
# query: 개발팀이 궁금해하는 문의조건 (and로 구분)

from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    
    ans = [0] * len(query)
    info_dict = {}    # 가능한 모든 경우의 수를 담기 위한 딕셔너리
    
    # info 정보를 스페이스 기준으로 구분                                            
    for men in info:
        tmp = men.split()
        info_key = tmp[:-1]  # 조합
        info_val = int(tmp[-1])   # 점수
        
        # 모든 경우의 수 만들어서 저장
        for i in range(5):
            for c in combinations(info_key, i):
                cc = ''.join(c)
                if cc in info_dict:    # 딕셔너리에 이미 해당 조합이 있다면, 그 조합에 value 추가
                    info_dict[cc].append(info_val)
                else:    # 없다면, 새로운 조합 생성
                    info_dict[cc] = [info_val]
    
    # info_dict의 values 정렬
    for i in info_dict:
        info_dict[i].sort()
    
    # 쿼리문 나누기 (and와 스페이스)
    for q in range(len(query)):
        
        # 먼저, 공백 기준으로 나눠 저장한 후, and와 - 제거
        msg = query[q].split()
        while 'and' in msg:
            msg.remove('and')
        while '-' in msg:
            msg.remove('-')
            
        msg_key = ''.join(msg[:-1])
        msg_val = int(msg[-1])
        
        if msg_key in info_dict:
            score = info_dict[msg_key]
            
            loc = bisect_left(score, msg_val)
            ans[q] += len(score) - loc
    
    return ans