s = input()
combs = set()

for i in range(1, len(s) + 1):
    for j in range(len(s) - i + 1):
        combs.add(s[j:j+i])
    
print(len(combs))