import sys

n = int(input())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

s = []

for i in arr:
    if i != 0:
        s.append(i)
    else:
        s.pop()
print(sum(s))
