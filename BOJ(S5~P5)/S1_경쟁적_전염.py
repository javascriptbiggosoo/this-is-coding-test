# https://www.acmicpc.net/problem/18405
# 1.5트 성공, 구현 넘나 어렵다

from collections import deque
from pprint import pprint

n, k = map(int, input().split())

판 = [list(map(int, input().split())) for _ in range(n)]

초, x, y = map(int, input().split())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


# 판 스캔, 숫자있는칸 좌표를 전부 리스트에 박아넣음
def scan():
    arr = []
    for r in range(n):
        for c in range(n):
            if 판[r][c]:  # 0 아닌경우
                arr.append([판[r][c], [r, c]])  # 숫자와 좌표를 담아줌
    return arr


# 숫자 오름차순으로 정렬 후 확산 1회 진행
def bfs(판, 초):
    q = deque([])
    arr = scan()
    arr.sort(key=lambda x: x[0])
    for i in arr:
        q.append(i)
    while 초:
        초 -= 1
        arr = []
        while q:
            curr = q.popleft()
            num = curr[0]
            r, c = curr[1]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and 판[nr][nc] == 0:
                    판[nr][nc] = num
                    arr.append([num, [nr, nc]])
        arr.sort(key=lambda x: x[0])
        for i in arr:
            q.append(i)


bfs(판, 초)
print(판[x - 1][y - 1])
