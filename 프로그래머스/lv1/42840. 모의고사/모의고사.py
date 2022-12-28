def solution(answers):
    ans = []
    
    students = [[1,2,3,4,5], 
                [2,1,2,3,2,4,2,5], 
                [3,3,1,1,2,2,4,4,5,5]]
    
    for i in range(len(students)):
        st = [students[i][j % len(students[i])] for j in range(len(answers))]
        
        for i in range(len(st)):
            st[i] = st[i] - answers[i]
        ans.append(st.count(0))
    print(max(ans))
    
    ans = [i + 1 for i in range(len(ans)) if ans[i] >= max(ans)]
            
    return ans