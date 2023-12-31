import sys
sys.stdin = open('input.txt', 'r')

w,h = int(input().split())
p,q = int(input().split())
t = int(input())

# 개미는 오른쪽 위 45도 방향으로 일정한 속력으로 움직이기 시작한다.
# 개미는 1시간 후에는 (p+1,q+1)로 옮겨간다. 

