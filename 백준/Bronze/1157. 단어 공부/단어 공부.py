T = input()
l=[]

for _ in range(26):
    l.append(0)

for i in range(0,len(T)):
    if ord(T[i]) >= 97:
        l[ord(T[i])-97] += 1
    else:
        l[ord(T[i])-65] += 1

max = l.index(max(l))
for i in range(max + 1, 26):
    if l[i] == l[max]:
        max = -1

if max == -1:
    print('?')
else:
    print(chr(max + 65))