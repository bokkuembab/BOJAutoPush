def solution(answers):
    
    students = [[1,2,3,4,5], 
                [2,1,2,3,2,4,2,5], 
                [3,3,1,1,2,2,4,4,5,5]]
    ans = [0, 0, 0]
    
    for i in range(len(students)):
        cycle = len(students[i])
        for j in range(len(answers)):
            if students[i][j % cycle] == answers[j]:
                ans[i] += 1

    ans = [i + 1 for i in range(len(ans)) if ans[i] == max(ans)]
            
    return ans