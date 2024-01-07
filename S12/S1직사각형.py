import sys
sys.stdin = open('input.txt', 'r')

# 왼쪽 아래 꼭짓점 좌표 (x, y) 오른쪽 위 꼭짓점 좌표 (p, q)
# 항상 x<p, y<q 이다.
for i in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = list(map(int,input().split()))

    # print(i+1,":",x1,y1,p1,q1,x2,y2,p2,q2)
    # 안겹침:d
    if x2 > p1 or p2 < x1 or q2 < y1 or y2 > q1:
        print("d")
    
    # 점:c
    elif x1==p2 or p1==x2:
        if y1==q2 or q1==y2:
            print("c")
        else:
            print("b")
    # 선분:b
    elif y1==q2 or q1==y2:
        print('b')
    # 직사각형:a
    else:
        print('a')