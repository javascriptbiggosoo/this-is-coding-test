import pprint

n = int(input())
arr = [[0] * n for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

arr[0][0] = n ** 2
cnt = n ** 2
방향 = 0
r = 0
c = 0
while cnt > 1:
    cnt -= 1
    nr = r + dr[방향]
    nc = c + dc[방향]
    if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
        arr[nr][nc] = cnt
    else:
        방향 = (방향 + 1) % 4
        nr = r + dr[방향]
        nc = c + dc[방향]
        arr[nr][nc] = cnt
    r = nr
    c = nc
target = int(input())

for i in range(n):
    for j in range(n):
        x = arr[i][j]
        if x == target:
            res = f"{i+1} {j+1}"
        if (j + 1) % n:
            print(x, end=" ")
        else:
            print(x)

print(res)