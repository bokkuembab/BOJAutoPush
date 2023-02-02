# N : 현재 캐릭터의 점수를 각 자리 숫자의 리스트로 만듬
N = list(map(int, input()))

a = sum(N[:len(N) // 2])
b = sum(N[len(N) // 2:])

if a == b:
    print("LUCKY")
else:
    print("READY")