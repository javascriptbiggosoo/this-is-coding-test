import sys

sys.stdin = open("개념_1의_갯수_세기.txt", "r")
# input
# 7(정사각형)
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000
#
# output: 2 13 (덩어리 당 1의 갯수)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(r, c):
    global cnt
    arr[r][c] = 0
    cnt += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # if arr[nr][nc] == 1 and width > nr >= 0 and width > nc >= 0:
        # 이건 안되네 ㅋㅋㅋㅋ 진기명기
        if width > nr >= 0 and width > nc >= 0 and arr[nr][nc] == 1:

            DFS(nr, nc)


width = int(input())
arr = [list(map(int, input())) for _ in range(width)]

for i in range(width):
    for j in range(width):
        if arr[i][j] == 1:
            cnt = 0
            DFS(i, j)
            print(cnt)
