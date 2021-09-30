# 1트, 답은 잘 나오는데 빅 시간초과

from collections import deque
import pprint

col, row = map(int, input().split())
arr = []

# 에너미컨트롤러
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(r, c):  # 무한으로 돌리지말고 한 번만 돌리래..
    arr[r][c] = 2
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nr < row and nc >= 0 and nc < col:
            if arr[nr][nc] == 0:
                arr[nr][nc] = 1


for i in range(row):
    arr.append(list(map(int, input().split())))

# print(arr)
날짜 = 0
영갯수 = 987654321
while True:
    # 0 하나도 없으면 탈출
    나가자 = 0
    for i in range(row):
        if 0 not in arr[i]:
            나가자 += 1
    if 나가자 == row:
        break

    # 익은곳마다 bfs 딱 한번 돌리기
    큐 = deque([])
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1:  # 현재 익은 토마토를 큐로
                큐.append([i, j])

    for i in range(len(큐)):
        토마토 = 큐.popleft()
        if arr[토마토[0]][토마토[1]] == 2:
            continue
        else:
            bfs(토마토[0], 토마토[1])  # 익히기

    # arr 0 갯수 세기, 하루 증가.
    이번영갯수 = 0
    for i in range(row):
        이번영갯수 += arr[i].count(0)

    날짜 += 1

    # 0 갯수 안바뀌면 탈출
    if 이번영갯수 == 영갯수:
        날짜 = -1
        break
    else:
        영갯수 = 이번영갯수

# pprint.pprint(arr)
print(날짜)
