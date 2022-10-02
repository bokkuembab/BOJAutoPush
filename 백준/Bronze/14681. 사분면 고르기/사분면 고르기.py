pX = int(input())
pY = int(input())

if pX > 0 and pY > 0:
    print(1)
elif pX < 0 and pY > 0:
    print(2)
elif pX < 0  and pY < 0:
    print(3)
else:
    print(4)