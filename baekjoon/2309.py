import sys

N = 9
shorts = []
for i in range(N):
    shorts+=list(map(int,sys.stdin.readline().split()))

num_sum = sum(shorts)
for i in range(N):
    target_num = 0
    for j in range(i+1,N):
        num_a = shorts[i]
        num_b = shorts[j]
        target_num = num_sum - (num_a + num_b)
        if target_num == 100:
            shorts.remove(num_a)
            shorts.remove(num_b)
            break
    if target_num == 100:
        break        
shorts.sort()
for i in range(len(shorts)):
    print(shorts[i])
