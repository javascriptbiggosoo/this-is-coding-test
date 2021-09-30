import pprint

T = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def dfs(r, c):
    arr[r][c] = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nr < row and nc >= 0 and nc < col and arr[nr][nc] == 1:
            dfs(nr, nc)


for tc in range(T):
    col, row, 인접 = map(int, input().split())

    arr = [[0] * col for _ in range(row)]

    for i in range(인접):
        c, r = map(int, input().split())
        arr[r][c] = 1
    # pprint.pprint(arr)
    ans = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1:
                dfs(i, j)
                ans += 1
    print(ans)
