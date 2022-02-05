import sys

loop = int(input())

lst = []
sum = 0

for i in range(loop):
    num, rg  = map(int, sys.stdin.readline().split())
    while(len(lst) > 0 and lst[-1] > rg):
        lst.pop()
        sum += 1

    if (len(lst) > 0 and lst[-1] == rg):
        continue
    if rg != 0 :
        lst.append(rg)

while(len(lst) > 0):
    sum +=1
    lst.pop()

print(sum)
