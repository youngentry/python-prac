import sys
sys.stdin = open('input.txt', 'r')

# 별4 동3 네2 세1
# 1. 별개수 다르면 -> 별 많은 승리
# 2. 별개수 같으면 -> 동 많은 승리
# 3. 별, 동 같으면 -> 네 많은 승리
# 4. 별, 동, 네 같으면 -> 세 많은 승리
# 5. 다 같으면 무승부

#  총 라운드 1 <= n <= 1000
#  a가 내는 총 개수 1 <= a <= 100
#  a개의 정수
#  동일한 방식으로 b

n = int(input())


for t_c in range(n):
    a_input =list(map(int, input().split()))
    b_input =list(map(int, input().split()))

    a = a_input[0]
    a_deck = sorted( a_input[1:], reverse=True)

    b = b_input[0]
    b_deck = sorted (b_input[1:], reverse=True)


    for i in range(4,0,-1):
        if a_deck.count(i) > b_deck.count(i):
            print("A")
            break
        elif a_deck.count(i) < b_deck.count(i):
            print("B")
            break
        if i==1:
            print("D")