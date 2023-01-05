# 조건 1. x(구하려는 숫자)는 자연수
# 조건 2. 2진수 변환 했을 때, n과 x의 1의 개수 같음
# 조건 3. x는 조건 1, 2를 만족하는 가장 작은 수

def solution(n):
    
    bigger = n + 1
    num1 = bin(n).count('1')
    
    while bigger > 0:
        if bin(bigger).count('1') == num1:
            break
        else:
            bigger += 1
    
    return bigger