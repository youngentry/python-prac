import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    days = int(input())
    prices = list(map(int,input().split()))
    
    plus = 0
    stack = []
    for i in range(days-1):
        if prices[i] > prices[i+1]:
            while(len(stack)):
                plus += prices[i]-stack.pop()
        else:
            stack.append(prices[i])

    while(len(stack)):
        plus += prices[-1]-stack.pop()

    print(f'#{test_case} {plus}')