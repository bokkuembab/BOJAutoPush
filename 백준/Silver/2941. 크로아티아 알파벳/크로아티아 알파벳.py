chr = input()
num = len(chr)

num -= (chr.count('=') + chr.count('-') )      # '=', '-'가 들어간 크로아티아 문자 찾음

for i in range(0, len(chr)-1):
    if chr[i] == 'l' or chr[i] == 'n':
        if chr[i+1] == 'j':
            num -= 1
    if i >= 1 and chr[i] == 'z':
        if chr[i-1] == 'd' and chr[i+1] == '=':
            num -= 1

print(num)