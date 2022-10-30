def solution(n, lost, reserve):
    
    # 모든 학생이 수업 가능한 것으로 초기화
    answer = n
    
    # 정렬
    lost.sort()
    reserve.sort()
    same = []
    
    # 여벌 있는데 도난당한 학생 먼저 제외
    for student in reserve:
        if student in lost:
            same.append(student)
    for s in same:
        lost.remove(s)
        reserve.remove(s)
    
    # 앞, 뒤 학생 확인
    for student in lost:
        if (student - 1) in reserve:
            reserve.remove(student - 1)
        elif (student + 1) in reserve:
            reserve.remove(student + 1)
        else:
            answer -= 1
    
    return answer