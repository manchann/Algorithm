import sys

n, k = map(int, sys.stdin.readline().split())

lst = []
for i in range(n):
    coin = int(sys.stdin.readline())
    lst.append(coin)

lst.sort(reverse=True)

sum = 0

for coin in lst:
    if coin > k:
        continue

    num = k // coin

    k -= coin * num

    sum +=num

    if k == 0:
        break
print(sum)
