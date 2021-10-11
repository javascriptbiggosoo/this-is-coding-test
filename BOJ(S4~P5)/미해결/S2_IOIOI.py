# 1트, 맞지만 시간초과로 50점
n = int(input())
m = int(input())
s = input()

pn = "I" + "OI" * n
cnt = 0
for i in range(m - n + 1):
    if s[i : 1 + i + 2 * n] == pn:
        cnt += 1

print(cnt)
