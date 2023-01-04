def solution(dartResult):
    
    ans = []
    dartResult = dartResult.replace('10', '-')
    scores = ['10' if i == '-' else i for i in dartResult]
    options = ['S', 'D', 'T']
    
    i = -1
    for o in scores:
        if o in options:
            ans[i] = ans[i] ** (options.index(o) + 1)
        elif o == '*':
            ans[i] *= 2
            if i != 0:
                ans[i-1] *= 2
        elif o == '#':
            ans[i] = ans[i] * (-1)
        else:
            ans.append(int(o))
            i += 1
    
    return sum(ans)