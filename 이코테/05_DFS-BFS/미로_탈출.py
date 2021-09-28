# 1트, 실~패~ 도는건 어찌되겠는데 최단거리 기록하는 법이 아리송송~~
from collections import deque

# 에너미 컨트롤러
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]  # 상우하좌


def bfs(시작점, arr):
    큐 = deque([시작점])
    row = 시작점[0]
    col = 시작점[1]
    arr[row][col] = 0
    mov = 0
    while arr[r - 1][c - 1] == 1:
        정점 = 큐.popleft()
        row = 정점[0]
        col = 정점[1]
        arr[row][col] = 0
        for i in range(4):
            if row + dr[i] >= 0 and row + dr[i] < r and col + dc[i] >= 0 and col + dc[i] < c:
                큐.append([row + dr[i], col + dc[i]])
        mov += 1
    return mov


r, c = map(int, input().split())
arr = []

for i in range(r):
    arr.append(list(map(int, input())))  # 이게 된다는걸 기억해두자 list뿐만아니라 iterable한건 다 된다는걸..

print(bfs([0, 0], arr))

# input
"""
5 6
101010
111111
000001
111111
111111
"""
