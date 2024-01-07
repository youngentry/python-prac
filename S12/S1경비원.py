import sys
sys.stdin = open('input.txt', 'r')

width, height = map(int,input().split())
n = int(input())

shops = []
for _ in range(n):
    shops.append(list(map(int,input().split())))

x,y = (map(int,(input().split())))

for _ in shops:
    s_x, s_y = shops

    
