import sys

nor = sys.stdin.readline().split('\n')[0]
secure = sys.stdin.readline().split('\n')[0]

cnt = 0
ans = ""

asci_num = 97
alph_num = 26
for i in range(len(nor)):
    if nor[i] == " ":
        cnt+=1
        cnt %= len(secure)
        ans+=" "
        continue
    target = ord(nor[i]) - ord(secure[cnt]) + alph_num - 1
    target %= 26
    ans+= chr(target + asci_num)
    cnt+=1
    cnt %= len(secure)

print(ans)
