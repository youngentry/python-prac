import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
targets = list(map(int, input().split()))
count = 0

numbers = [i for i in range(1,N+1)]

# 2번 연산
def toLeft():
    left = numbers.pop(0)
    numbers.append(left)

# 3번 연산
def toRight():
    right = numbers.pop()
    numbers.insert(0,right)

while(len(targets)):
    # 1번 연산
    if targets[0] == numbers[0]:
        targets.pop(0)
        numbers.pop(0)
        continue
    
    # 타겟 인덱스 찾기 9
    target_index = numbers.index(targets[0])
    half = len(numbers)//2

    if (target_index > half):
        while targets[0] != numbers[0]:
            toRight()
            count+=1
    else:
        while targets[0] != numbers[0]:
            toLeft()
            count+=1

print(count)