import sys
sys.stdin = open('input.txt', 'r')

# input 1 가로세로
# input 2 자를 횟수
# input... 가로:0 세로:1 번호

n,m = map(int,input().split())
cut_count = int(input())

area = [0,0, n,m]

for t_c in range(cut_count):
    direction, number = map(int,input().split())

    # 큰면적의 x,y를 기록하기
    x1,y1,x2,y2 = area
    # print(area)

    if direction==0 and number >= y1 and number < y2:
        if number > (y2+y1)/2:
            area[3] = number
        else:
            area[1] = number

    if direction==1 and number >= x1 and number < x2:
        if number > (x2+x1)/2:
            area[2] = number
        else:
            area[0] = number
    print(area)
    print((area[3]-area[1]) * (area[2]-area[0]))


# print(area)
print((area[3]-area[1]) * (area[2]-area[0]))