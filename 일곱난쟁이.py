import sys

# 표준 입력을 input.txt 파일로 변경
sys.stdin = open('input.txt', 'r')

lists = []
for _ in range(9):
    lists.append(int(input()))

lists.sort()

height_sum = sum(lists)

found = False
for i in range(9):
    if found:
        break
    for j in range(i+1,9):
        if (height_sum - lists[i] - lists[j]) == 100:
            except1, except2 = lists[i], lists[j]
            found = True
            break


for height in lists:
    if (height != except1 and height != except2):
        print(height)