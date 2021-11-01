# 2트, 이중포문은 가장 바깥에서 break를 해줘야합니다..
# 이 문제는 7576번 토마토의 심화판임
from collections import deque
import pprint


# 에너미컨트롤러
da = [0, 0, 0, 0, 1, -1]
dr = [0, 0, 1, -1, 0, 0]
dc = [1, -1, 0, 0, 0, 0]


def bfs(큐):
    while len(큐):
        a, r, c = 큐.popleft()
        for i in range(6):
            na = a + da[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if (
                na >= 0
                and na < 판
                and nr >= 0
                and nr < row
                and nc >= 0
                and nc < col
                and arr[na][nr][nc] == 0
            ):
                큐.append([na, nr, nc])
                arr[na][nr][nc] = arr[a][r][c] + 1  # 날짜 이걸로 맞출생각


col, row, 판 = map(int, input().split())

arr = []
for i in range(판):
    arr.append([])
    for j in range(row):
        arr[i].append(list(map(int, input().split())))


큐 = deque([])  # 첫 토마토들 큐에 박기
for i in range(판):
    for j in range(row):
        for k in range(col):
            if arr[i][j][k] == 1:
                큐.append([i, j, k])

bfs(큐)
# pprint.pprint(arr)

ans = -1
나가자 = False
for i in range(판):
    if 나가자:  ############################### 1트에서 이걸 안함
        break
    for j in range(row):
        if 0 in arr[i][j]:
            ans = -1
            나가자 = True
            break
        if ans < max(arr[i][j]):
            ans = max(arr[i][j]) - 1  # 0일째부터 1 먹고가니깐

print(ans)  # 토마토가 없는 빈상자라면?


# # 1트, 진짜 왜틀리는지 모르겠다..
# from collections import deque
# import pprint


# # 에너미컨트롤러
# da = [0, 0, 0, 0, 1, -1]
# dr = [0, 0, 1, -1, 0, 0]
# dc = [1, -1, 0, 0, 0, 0]


# def bfs(큐):
#     while len(큐):
#         a,r,c = 큐.popleft()
#         for i in range(6):
#             na = a + da[i]
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if (
#                 na >= 0
#                 and na < 판
#                 and nr >= 0
#                 and nr < row
#                 and nc >= 0
#                 and nc < col
#                 and arr[na][nr][nc] == 0
#             ):
#                 큐.append([na, nr, nc])
#                 arr[na][nr][nc] = arr[a][r][c] + 1  # 날짜 이걸로 맞출생각


# col, row, 판 = map(int, input().split())

# arr = []
# for i in range(판):
#     arr.append([])
#     for j in range(row):
#         arr[i].append(list(map(int, input().split())))


# 큐 = deque([])  # 첫 토마토들 큐에 박기
# for i in range(판):
#     for j in range(row):
#         for k in range(col):
#             if arr[i][j][k] == 1:
#                 큐.append([i, j, k])

# bfs(큐)
# # pprint.pprint(arr)

# ans = -1
# for i in range(판):
#     for j in range(row):
#         if 0 in arr[i][j]:
#             ans = -1
#             break
#         if ans < max(arr[i][j]):
#             ans = max(arr[i][j]) - 1  # 0일째부터 1 먹고가니깐

# print(ans)  # 토마토가 없는 빈상자라면?
