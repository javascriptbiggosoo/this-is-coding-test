# 1트, 큐2를 먼저 풀었는데 그 코드랑 똑같이 하니까 정답임;
import sys
from collections import deque

n = int(input())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]

# print(arr)
q = deque([])

for i in arr:
    if i[:2] == "pu":
        q.append(i[5:])
    elif i == "pop":
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif i == "size":
        print(len(q))
    elif i == "empty":
        if len(q):
            print(0)
        else:
            print(1)
    elif i == "front":
        if len(q):
            print(q[0])
        else:
            print(-1)
    else:
        if len(q):
            print(q[-1])
        else:
            print(-1)
