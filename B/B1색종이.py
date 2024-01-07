# 색종이의 장수 N 1~100
# 평면은 가로 1001, 세로 1001

# 왼쪽아래 x,y 너비 width,height
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

grid = [[0 for _ in range(1001)] for _ in range(1001)]

for t_c in range(n):
    x,y,width,height = map(int,input().split())
    for i in range(x,x+width):
        for j in range(y,y+height):
            grid[i][j] = t_c+1

answers = [0] * n
for row in grid:
    for number in row:
        if number:
            answers[number-1] +=1


for width in answers:
    print(width) 
