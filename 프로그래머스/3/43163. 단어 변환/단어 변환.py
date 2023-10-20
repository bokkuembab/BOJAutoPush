from collections import deque

def solution(begin, target, words):
    
    # 리스트에 목표 단어가 없으면, 종료
    if target not in words:
        return 0
    
    ans = 0    # 변환횟수
    visited = [False] * len(words)    # 방문 리스트
    q = deque([(begin, ans)])    # 시작 단어로 큐 초기화

    while q:
        now, cnt = q.popleft()
        
        for idx, w in enumerate(words):
            
            if now == target:    # 목표한 단어에 도달하면,
                ans = cnt    # 변환 횟수 수정 후 반복 종료
                break
            
            if not visited[idx]:    # 방문하지 않았다면,
                diff = len([i for i, j in zip(now, w) if i != j])    # 다른 글자의 수
                if diff == 1:    # 글자가 하나만 다르다면,
                    q.append((w, cnt + 1))    # q에 넣어주기
                    visited[idx] = True    # 방문처리
    
    return ans