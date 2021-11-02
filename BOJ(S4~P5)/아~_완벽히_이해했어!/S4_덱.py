# https://www.acmicpc.net/problem/10866
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
덱 = deque([])
for i in range(n):
    k = sys.stdin.readline().rstrip()
    if k[:6] == "push_f":
        덱.appendleft(k[11:])
    elif k[:6] == "push_b":
        덱.append(k[10:])
    elif k[:5] == "pop_f":
        if 덱:
            print(덱.popleft())
        else:
            print(-1)
    elif k[:5] == "pop_b":
        if 덱:
            print(덱.pop())
        else:
            print(-1)
    elif k == "size":
        print(len(덱))
    elif k == "empty":
        if 덱:
            print(0)
        else:
            print(1)
    elif k == "front":
        if 덱:
            print(덱[0])
        else:
            print(-1)
    elif k == "back":
        if 덱:
            print(덱[-1])
        else:
            print(-1)
