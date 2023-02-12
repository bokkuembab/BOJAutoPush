# word_n: 단어의 개수, word_li: 입력받은 단어 저장 집합(set)

word_n = int(input())
word_li = set()    # 중복을 제거하기 위해 집합 자료형으로 생성
for _ in range(word_n):
    word_li.add(input())
    
word_li = sorted(word_li, key=lambda w: [len(w), w])    # 길이순, 사전순 기준으로 정렬

for w in word_li:    # 하나씩 출력
    print(w)