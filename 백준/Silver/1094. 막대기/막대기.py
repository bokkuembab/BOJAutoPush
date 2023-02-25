goal = int(input())       # 막대기의 목표 길이

# 막대를 잘라 -> 64->32 32->32 16 16->32 16 8 8
st = []   # 막대의 길이를 저장하고 있는 스택
st.append(64)       # 처음 막대의 길이 저장

while sum(st) != goal:
    tmp = st.pop() // 2
    st.append(tmp)
    
    if sum(st) < goal:
        st.append(tmp)
    
    
print(len(st))