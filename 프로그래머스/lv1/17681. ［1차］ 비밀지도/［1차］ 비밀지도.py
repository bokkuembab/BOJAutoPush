def solution(n, arr1, arr2):
    answer = []
    l = len(bin(max(max(arr1), max(arr2)))[2:])
    
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        arr1[i] = (l - len(arr1[i])) * '0' + arr1[i]
        arr2[i] = bin(arr2[i])[2:]
        arr2[i] = (l - len(arr2[i])) * '0' + arr2[i]
            
        tmp = ''
        for j in range(n):
            if int(arr1[i][j]) + int(arr2[i][j]) > 0:
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer