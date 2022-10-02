up, down, height = map(int, input().split())

res = (height-up) / (up-down)
if res == int(res):
    print(int(res) + 1)
else:
    print(int(res) + 2)