# 1트, 실패.. 먼가 먼가 틀림 테스트 케이스 일부만 마즘

from collections import deque
import pprint

n = int(input())

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

arr = [list(map(int, input().split())) for _ in range(n)]
temp_arr = [[0] * n for _ in range(n)]

size = 2

fish = []
for r in range(n):
    for c in range(n):
        if arr[r][c] > 0:
            if arr[r][c] == 9:
                arr[r][c] = 0
                row = r
                col = c
                continue
            fish.append(arr[r][c])

fish.sort()
fish = deque(fish)  # 식사후 또 먹을 수 있는지 이걸로 확인


def bfs(arr, row, col, size):
    q = deque([[row, col]])
    candidate = []
    먹을시간 = False
    while q:
        if 먹을시간:
            # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
            candidate.sort(key=lambda x: (-x[0], -x[1]))
            # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
            return candidate[0]
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 아기 상어는 자신보다 큰 물고기가 있는 칸은 지나갈 수 없고,
            # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
            if 0 <= nr < n and 0 <= nc < n and size >= arr[nr][nc]:
                q.append([nr, nc])
                # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
                temp_arr[nr][nc] = temp_arr[r][c] + 1
                # 자신보다 작은 물고기만 먹을 수 있다.
                if 0 < arr[nr][nc] < size:
                    candidate.append([nr, nc, temp_arr[nr][nc]])
                    if candidate[0][2] != temp_arr[nr][nc]:
                        candidate.pop()
                        먹을시간 = True


sec = 0
eat = 0
while True:
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if len(fish) == 0 or size <= fish[0]:
        break
    fish.popleft()
    # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    row, col, 초 = bfs(arr, row, col, size)
    eat += 1
    sec += 초
    arr[row][col] = 0
    temp_arr[row][col] = 0
    # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
    pprint.pprint(arr)
    if eat == size:
        size += 1
        eat = 0

# 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
print(sec)
