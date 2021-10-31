# 1트 성공, 조건 제대로 확인 못해서 수정에 수정을 했다.
# 1. 입력 받자마자 방향 전환 하는줄 알았고
# 2. 이전 명령 후가 아니라 시작 시간기준이었고
# 3. 모든 명령이 끝나도 가던 길 계속 가도록 처리해야했다.
# 문제를 잘 읽자..

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
# 처음엔 오른쪽
방향 = 0
while 뱀:
    # ctrl 확인, 마감되면 방향틀고 다음 ctrl 넣기
    if ctrl[0] == sec:
        if ctrl[1] == "D":
            방향 += 1
            if 방향 >= 4:
                방향 -= 4
        else:
            방향 -= 1
            if 방향 < 0:
                방향 += 4
        try:
            ctrl = EC.popleft()
        except:
            None
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
        # pprint.pprint(판)
        # print(ctrl)
    # 진행(사과)
    elif (
        머리[0] + dr[방향] > 0
        and 머리[0] + dr[방향] <= n
        and 머리[1] + dc[방향] > 0
        and 머리[1] + dc[방향] <= n
        and 판[머리[0] + dr[방향]][머리[1] + dc[방향]] == 9
    ):
        뱀.append([머리[0] + dr[방향], 머리[1] + dc[방향]])
        판[머리[0] + dr[방향]][머리[1] + dc[방향]] = 1
        # pprint.pprint(판)
        # print(ctrl)
    # 게임오버
    else:
        break


print(sec)
