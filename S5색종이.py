import sys
sys.stdin = open('input.txt', 'r')

# 가로 세로 100 도화지

# 가로 세로 10인 정사각형 붙임

n = int(input())
big_paper = [[0 for _ in range(100)] for _ in range(100)]

for small_paper in range(n):
    x,y = map(int,input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            big_paper[i][j] = 1

print(sum([sum(array) for array in big_paper]))
