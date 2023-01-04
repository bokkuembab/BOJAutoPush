def solution(dartResult):
    # 게임은 3번, 0~10점
    # S, D, T: 1, 2, 3 제곱
    # *스타상 / #아차상 : 해당 점수, 바로 전 점수 2배 / 해당 점수 마이너스
    
    ans = []
    scores = [str(i) for i in range(0, 10)]
    
    # 3회의 dart 나누기
    for i in range(2, len(dartResult)):
        if dartResult[i] == '1' and dartResult[i:i+2] == '10':
            continue
        
        if dartResult[i] == '0' and dartResult[i-1:i+1] == '10':
            ans.append(dartResult[:i-1])
        elif dartResult[i] in scores:
            ans.append(dartResult[:i])
    
    ans.append(dartResult.replace(ans[1], ""))
    ans[1] = ans[1].replace(ans[0], "")
    
    for time, dart in enumerate(ans):
        print(time, dart)
        if dart[1] == '0':
            ans[time], i = int(dart[:2]), 2
        else:
            ans[time], i = int(dart[0]), 1
            
        
        if dart[i:i+1] == 'D':
            ans[time] = ans[time] ** 2
        elif dart[i:i+1] == 'T':
            ans[time] = ans[time] ** 3
            
        if dart[i+1:i+2] == '*':
            ans[time-1] *= 2
            ans[time] *= 2
        elif dart[i+1:i+2] == '#':
            ans[time] = -ans[time]
    
    
    return sum(ans)