from math import log2

def is_tree(num_bin, prev_parent):
    
    # 중앙값(자손) 기준으로 재귀적으로 확인
    mid = len(num_bin) // 2
    if num_bin:   # 자식이 더 존재할 때,
        child = (num_bin[mid] == '1')   # '1'인 요소가 있는지 (더 뻗어나가야 하는지)
    else: 
        return True
    
    # 현재 리스트의 '1'인 자식이 존재하므로, 부모가 존재해야함.
    if child and not prev_parent:
        return False
    else:    # 자식의 양쪽 자식 노드들 재귀
        return is_tree(num_bin[mid + 1:], child) and is_tree(num_bin[:mid], child)

def solution(numbers):
    ans = []
    
    for n in numbers:
        # 1. 주어진 수를 이진수로 변환하기
        binn = bin(n)[2:]
        
        # 2. 포화 이진 트리의 노드 수만큼 늘려주기
        tmp = int(log2(len(binn))) + 1
        digit = 2 ** tmp - 1
        binn = "0" * (digit - len(binn)) + binn
        
        # 3. 부모 노드가 '1'인지 확인
        if binn[len(binn) // 2] != '1':
            ans.append(0)
            continue
        
        # 4. 부모 노드의 자식 노드들을 재귀적으로 확인하며, 부모 노드가 '1'인지 확인
        if is_tree(binn, True):
            ans.append(1)
            continue
            
        ans.append(0)
    
    return ans