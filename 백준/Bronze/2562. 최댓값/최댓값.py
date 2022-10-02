lt=[]

for _ in range(9):
    lt.append(int(input()))

print(max(lt), lt.index(max(lt))+1)