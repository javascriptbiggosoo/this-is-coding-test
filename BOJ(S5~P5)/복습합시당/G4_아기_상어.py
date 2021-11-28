# https://www.acmicpc.net/problem/16236

# 4,5,6트 정도, 걸림
# if dists[r][c] != -1 and arr[r][c] and size > arr[r][c] and dists[r][c] < dist: 이거 and 사이사이 순서도 속도에 영향 줌  다른 자잘한거도.. 신경 쓸거.. 매우 많음................후........... 꼭 해부, 복습 필수

# 구현도 구현이지만, 우선 처음부터 코드의 로직을 잘 구상해봐야한다는..
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

INF = 1e9


size = 2
curr_r = 0
curr_c = 0

for r in range(n):
    for c in range(n):
        if arr[r][c] == 9:
            curr_r, curr_c = r, c
            arr[curr_r][curr_c] = 0

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def find(dists):
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    curr_c, curr_r = 0, 0
    dist = INF
    for r in range(n):
        for c in range(n):
            if dists[r][c] != -1 and arr[r][c] and size > arr[r][c] and dists[r][c] < dist:
                dist = dists[r][c]
                curr_r = r
                curr_c = c
    # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    # 자신보다 작은 물고기만 먹을 수 있다.
    return (curr_r, curr_c, dist)


def bfs():
    dists = [[-1] * n for _ in range(n)]
    q = deque([(curr_r, curr_c)])
    dists[curr_r][curr_c] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 아기 상어는 자신보다 큰 물고기가 있는 칸은 지나갈 수 없고,
            # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
            if 0 <= nr < n and 0 <= nc < n and dists[nr][nc] == -1 and arr[nr][nc] <= size:
                dists[nr][nc] = dists[r][c] + 1
                q.append((nr, nc))
                # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    return dists


sec = 0
ate = 0
while True:
    # 거리가 가장 가까운 물고기를 먹으러 간다.
    curr_r, curr_c, dist = find(bfs())
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if dist == 1e9:
        break
    ate += 1
    sec += dist
    arr[curr_r][curr_c] = 0
    # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
    if ate >= size:
        size += 1
        ate = 0

# 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지
print(sec)


# 1트, 실패.. 먼가 먼가 틀림 테스트 케이스 일부만 마즘
# 1트, 실패.. 먼가 먼가 틀림 테스트 케이스 일부만 마즘

# from collections import deque
# import pprint

# n = int(input())

# dr = [-1, 0, 0, 1]
# dc = [0, -1, 1, 0]

# arr = [list(map(int, input().split())) for _ in range(n)]
# temp_arr = [[0] * n for _ in range(n)]

# size = 2

# fish = []
# for r in range(n):
#     for c in range(n):
#         if arr[r][c] > 0:
#             if arr[r][c] == 9:
#                 arr[r][c] = 0
#                 row = r
#                 col = c
#                 continue
#             fish.append(arr[r][c])
# # 식사후 또 먹을 수 있는지 이걸로 확인
# fish.sort()
# fish = deque(fish)


# def bfs(arr, row, col, size):
#     q = deque([[row, col]])
#     candidate = []
#     먹을시간 = False
#     while q:
#         if 먹을시간:
#             # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
#             candidate.sort(key=lambda x: (x[0], x[1]))
#             # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
#             return candidate[0]
#         r, c = q.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             # 아기 상어는 자신보다 큰 물고기가 있는 칸은 지나갈 수 없고,
#             # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
#             if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] <= size:
#                 q.append([nr, nc])
#                 # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
#                 temp_arr[nr][nc] = temp_arr[r][c] + 1
#                 # 자신보다 작은 물고기만 먹을 수 있다.
#                 if 0 < arr[nr][nc] < size:
#                     candidate.append([nr, nc, temp_arr[nr][nc]])
#                     먹을시간 = True


# sec = 0
# ate = 0
# while True:
#     # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
#     if len(fish) == 0 or size <= fish[0]:
#         break
#     fish.popleft()
#     # 거리가 가장 가까운 물고기를 먹으러 간다.
#     row, col, 초 = bfs(arr, row, col, size)
#     ate += 1
#     sec += 초
#     arr[row][col] = 0
#     temp_arr[row][col] = 0
#     # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
#     if ate == size:
#         size += 1
#         ate = 0

# # 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지
# print(sec)
