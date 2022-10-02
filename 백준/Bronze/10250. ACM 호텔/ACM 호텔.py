test = int(input())

for i in range(test):
    height, room, guest = map(int, input().split())
    if guest % height == 0:
        print("{0:d}{1:02d}".format(height, guest // height))
    else:
        print("{0:d}{1:02d}".format(guest % height, guest // height + 1))