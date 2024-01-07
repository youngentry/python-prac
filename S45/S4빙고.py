import sys
sys.stdin = open('input.txt', 'r')

numbers = []

for i in range(5):
    numbers.append(input().split())


calls = ""

for i in range(5):
    calls += input()+" "

call_numbers = calls.split() 

for i in range(0,25):
    # 호출된 번호 "O"로 변경
    for j in range(5):
        for k in range(5):
            if numbers[j][k]==str(call_numbers[i]):
                numbers[j][k] = "O"

    count = 0
    ex1 = ""
    ex2 = ""
    for j in range(5):
        col = ""
        # 가로 확인
        row = "".join(numbers[j])
        if row == "OOOOO":
            count += 1

        # 세로, 대각선 확인
        for k in range(5):
            if numbers[k][j]=="O":
                col += numbers[k][j]
            if j==k:
                ex1 += numbers[j][k]
            if j+k==4:
                ex2 += numbers[j][k]
                

            if col=="OOOOO":
                count +=1

        if ex1=="OOOOO":
            count +=1
        if ex2=="OOOOO":
            count +=1

    # 한 번에 여러개의 빙고가 만들어질 수 있음
    if count >= 3:
        print(i+1)
        break
        