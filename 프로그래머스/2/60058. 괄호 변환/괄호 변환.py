# 올바른 괄호인지 확인하는 함수
def is_correct(p):
    stack = []
    for i in p:
        # 스택이 비어있고, 여는 괄호면 추가
        if not stack:    
            if i == ')':    # 닫는 괄호면, 성립 X -> 종료
                return False
            stack.append(i)
            continue
            
        # 괄호가 닫혔으면, 스택에서 제거
        if stack[-1] != i:    
            stack.pop()
        else:
            stack.append(i)
    
    if stack:
        return False
    else:
        return True

# 올바른 괄호로 변환하는 함수
def make_correct(p):
    # 1. 빈 문자열 반환
    if not p:
        return p
    
    # 2. u, v 분리
    for i in range(1, len(p) + 1):
        if p[:i].count('(') == p[:i].count(')'):
            sep = i
            break
    u, v = p[:sep], p[sep:]
    
    # 3. u가 올바른 괄호 문자열일 경우
    if is_correct(u):
        return u + make_correct(v)
    # 4. u가 올바른 괄호 문자열이 아닐 경우
    else:
        u = u[1:-1]
        u = ['(' if u[i] == ')' else ')' for i in range(len(u))]
        u = ''.join(u)
        return '(' + make_correct(v) + ')' + u
    
def solution(p):
    
    # 올바른 괄호인지 확인
    if is_correct(p):
        return p
    
    # 올바른 괄호로 변환
    return make_correct(p)
