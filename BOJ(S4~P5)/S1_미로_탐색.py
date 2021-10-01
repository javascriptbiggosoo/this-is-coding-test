# 1트 성공, 다풀어놓고 오랜만에 입력을 잘못 받아서 한참 헤맸다;;;;
from collections import deque

row, col = map(int, input().split())


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(x, y):
    큐 = deque([[x, y]])
    arr[x][y] = 1  # 이거 첫부분 되돌아오면서 arr 시작점이 3이 되긴하는데 끝점만 보면 되니깐 상관무
    while len(큐):
        r, c = 큐.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < row and 0 <= nc < col and arr[nr][nc] == 1:
                큐.append([nr, nc])
                arr[nr][nc] = arr[r][c] + 1


arr = []
for i in range(row):
    arr.append(list(map(int, input())))  # 입력.. 붙어서 나옴.. split() 안하면됨..


bfs(0, 0)
print(arr[row - 1][col - 1])
