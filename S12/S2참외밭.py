import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

# 1동 2서 3남 4북
l_r = []
t_b = []


for width in range(6):
    direction, size =map(int, input().split())
    if direction == 1 or direction== 2:
        l_r.append(size)
    else:
        t_b.append(size)


max_t = max(t_b) 
max_l = max(l_r)

max_t_idx = t_b.index(max_t)
max_l_idx = l_r.index(max_l)
# ㄱ 이면
# max가 0,0
if max_t_idx == 0 and max_l_idx == 0:
    print((t_b[max_t_idx]*l_r[max_l_idx] - (t_b[2]*l_r[1]))*n)

# ┏ 이면
# max가 0,2
if max_t_idx == 0 and max_l_idx == 2:
    print((t_b[max_t_idx]*l_r[max_l_idx] - (t_b[1]*l_r[1]))*n)

# ┗ 이면
# max가 2,2 
if max_t_idx == 2 and max_l_idx == 2:
    print((t_b[max_t_idx]*l_r[max_l_idx] - (t_b[1]*l_r[0]))*n)
    
# ┛ 이면
# max가 2,0
if max_t_idx == 2 and max_l_idx == 1:
    print((t_b[max_t_idx]*l_r[max_l_idx] - (t_b[0]*l_r[0]))*n)
