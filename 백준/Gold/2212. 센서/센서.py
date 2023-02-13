import sys
input = sys.stdin.readline

sen = int(input())    # sen_num: 센서의 개수
net = int(input())    # net_num: 집중국의 개수
sen_list = list(map(int, input().split()))    # net_list: 센서 좌표 리스트
dist_list =[]    # 센서간의 거리 저장 리스트

sen_list.sort()    # 센서 위치 순서대로 정렬

for i in range(0, sen - 1):   # 센서 간의 거리 계산
    dist_list.append(sen_list[i + 1] - sen_list[i])
    
dist_list.sort()    # 센서 간 거리 리스트 정렬
print(sum(dist_list[:sen - net]))    # 가장 거리가 먼 구간부터 센서 배치