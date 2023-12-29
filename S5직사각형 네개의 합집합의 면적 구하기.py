import sys
# 표준 입력을 input.txt 파일로 변경
sys.stdin = open('input.txt', 'r')

# 왼쪽아래 (a,b) 오른쪽위 (c,d)

# 0으로 채운 이차원 배열

maps = [[0 for _ in range(100)] for _ in range(100)]


for test_case in range(4):
    a,b,c,d = map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            maps[i][j] = 1


print(sum([sum(row) for row in maps]))

    