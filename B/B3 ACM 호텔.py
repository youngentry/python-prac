# 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호
# W 개의 방이 있는 H 층 건물 (1~99)
# 엘리베이터는 가장 왼쪽

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for T_C in range(1,T+1):
    H, W, N = map(int,input().split())
    
    # 호텔 크기 만큼의 이차원 배열 생성
    hotel = [[0 for _ in range(W)] for _ in range(H)]

		# 호텔과 똑같이 방 배정
    for i in range(H):
        for j in range(W):
            hotel[i][j] += (i+1)*100 + j+1
    
    # N번째 방문한 손님이 어느 방에 묵게 될지 확인
    print(hotel)
    count = 0
    for i in range(W):
        for j in range(H):
            count+=1
            if (count==N):
                print(hotel[j][i])