# 1트 성공, 다풀어놓고 오랜만에 입력을 잘못 받아서 한참 헤맸다;;;;
from collections import deque

n = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


# dfs 안에서 재귀, 혹은 방문체크 한 번 당 +=1로 덩어리 단지 수 세기
def dfs(r, c):
    global ans
    ans += 1
    arr[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 1:
            dfs(nr, nc)


arr = []
for i in range(n):
    arr.append(list(map(int, input())))

# arr 순회하면서 한 덩어리당 dfs 한 번, 찍은곳은 0으로 바꿔줌
덩어리 = 0
res = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            ans = 0
            dfs(i, j)
            덩어리 += 1
            res.append(ans)

print(덩어리)
res.sort()
for i in res:
    print(i)
