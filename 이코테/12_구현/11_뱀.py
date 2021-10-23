# https://www.acmicpc.net/problem/3190
import sys
from collections import deque
import pprint

n = int(sys.stdin.readline().rstrip())
판 = [[0] * (n + 1) for _ in range(n + 1)]
# 사과 수
k = int(sys.stdin.readline().rstrip())
for i in range(k):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    판[r][c] = 9
판[1][1] = 1
# 방향 전환
l = int(sys.stdin.readline().rstrip())
# 에너미 컨트롤러
EC = deque([])
for i in range(l):
    t, c = sys.stdin.readline().rstrip().split()
    EC.append([int(t), c])

뱀 = deque([[1, 1]])
dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]
# 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
sec = 0
ctrl = EC.popleft()
방향 = 0
if ctrl[1] == "D":
    방향 += 1
    if 방향 >= 4:
        방향 -= 4
else:
    방향 -= 1
    if 방향 < 0:
        방향 += 4

while 뱀:
    sec += 1
    머리 = 뱀[-1]
    # 진행
    if (
        머리[0] + dr[방향] > 0
        and 머리[0] + dr[방향] <= n
        and 머리[1] + dc[방향] > 0
        and 머리[1] + dc[방향] <= n
        and 판[머리[0] + dr[방향]][머리[1] + dc[방향]] == 0
    ):
        뱀.append([머리[0] + dr[방향], 머리[1] + dc[방향]])
        판[머리[0] + dr[방향]][머리[1] + dc[방향]] = 1
        꼬리 = 뱀.popleft()
        판[꼬리[0]][꼬리[1]] = 0
        pprint.pprint(판)
        print(ctrl)
    # 진행+사과
    elif (
        머리[0] + dr[방향] > 0
        and 머리[0] + dr[방향] <= n
        and 머리[1] + dc[방향] > 0
        and 머리[1] + dc[방향] <= n
        and 판[머리[0] + dr[방향]][머리[1] + dc[방향]] == 9
    ):
        뱀.append([머리[0] + dr[방향], 머리[1] + dc[방향]])
        판[머리[0] + dr[방향]][머리[1] + dc[방향]] = 1
        pprint.pprint(판)
        print(ctrl)
    # 게임오버
    else:
        break
    # ctrl 확인
    ctrl[0] -= 1
    if ctrl[0] <= 0:
        ctrl = EC.popleft()
        if ctrl[1] == "D":
            방향 += 1
            if 방향 >= 4:
                방향 -= 4
        else:
            방향 -= 1
            if 방향 < 0:
                방향 += 4

print(sec)
