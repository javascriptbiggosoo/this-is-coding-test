import sys

듣, 보 = map(int, sys.stdin.readline().rstrip().split())

ㄷ = []
for i in range(듣):
    ㄷ.append(sys.stdin.readline().rstrip())

ㅂ = []
for i in range(보):
    ㅂ.append(sys.stdin.readline().rstrip())


cnt = 0
ans = []
for i in ㄷ:
    if i in ㅂ:
        ans.append(i)
        cnt += 1

print(cnt)
for i in ans:
    print(i)
