import sys

# 표준 입력을 input.txt 파일로 변경
sys.stdin = open('input.txt', 'r')

# 이제 input() 호출은 input.txt 파일에서 데이터를 읽습니다.
n,k = map(int,input().split())

students = {}
for test_case in range(1, n + 1):
    s,y = input().split()

    unit = ""
    if int(s)==1:
        unit = "m" + y
    else:
        unit = 'w' + y

    if unit not in students:
        students[unit] = 1
    else:
        students[unit] = students[unit] + 1

room_count = 0
for count in students.values():
    while count>0:
        count -= k
        room_count += 1

print(room_count)
# 첫 줄에 학생 수 n, 한 방 인원 k
# 성별 s, 학년 y