# 입력 받기
str = input()

# 먼저 태그로 나눠서, 단어만 분리
i = 0    # 서치 인덱스
res = ''
while i < len(str):

    # 태그이면, 그대로 넣기
    if str[i] == '<':
        res += str[i]
        i += 1
        while True:
            if str[i] == '>':
                res += str[i]
                i += 1
                break
            res += str[i]
            i += 1
    # 단어이면, 뒤집어주기
    else:
        word = ''   # 단어만 분리할 문자열
        while str[i] != '<':
            word += str[i]
            i += 1
            if i > len(str) - 1:
                break
        # 단어 나눔
        tmp = word.split()
        for k in range(len(tmp)):
            res += tmp[k][-1::-1]
            if k != len(tmp) - 1:
                res += ' '
        
print(res)