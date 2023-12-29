import sys

# 표준 입력을 input.txt 파일로 변경
sys.stdin = open('input.txt', 'r')

# n명의 학생이 줄 서기

# 줄 선 학생들이 차례로 뽑은 번호

n = int(input())
tickets = input().split()

lines = [i+1 for i in range(n)]

for i in range(n):
    current_number = lines.pop(i)
    lines.insert(i - int(tickets[i]), current_number)

print(" ".join(map(str,lines)))