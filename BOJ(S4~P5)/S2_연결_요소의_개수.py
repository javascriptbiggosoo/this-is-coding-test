# 2트 성공, python은 재귀 횟수 제한이 있어서 실패하는데 pypy에선 정답됨; 하튼 구현 연습이 필요한건 확실
import sys


정점수, 간선수 = map(int, sys.stdin.readline().rsplit())

간선들 = [list(map(int, sys.stdin.readline().rsplit())) for i in range(간선수)]
# print(간선들)
arr = [[] for i in range(정점수 + 1)]
for 간선 in 간선들:
    st, ed = 간선
    arr[st].append(ed)
    arr[ed].append(st)
visited = [0] * (정점수 + 1)

# pprint.pprint(arr)

res = 0


def dfs(v):
    visited[v] = 1
    for el in arr[v]:
        if visited[el] == 0:
            dfs(el)


for i in range(1, 정점수 + 1):
    if visited[i] == 0:
        dfs(i)
        # print(visited)
        res += 1

print(res)


# 1트 실패, dfs bfs 다해봤는데 재귀 초과, 시간초과, 메모리초과 다 걸리고 구현 자체도 오랜만에 하다보니 오래 걸렸다 댐 ㅠㅠ
# import sys, pprint
# from collections import deque

# 정점수, 간선수 = map(int, sys.stdin.readline().rsplit())

# 간선들 = [list(map(int, sys.stdin.readline().rsplit())) for i in range(간선수)]
# # print(간선들)
# arr = [[] for i in range(정점수 + 1)]
# for 간선 in 간선들:
#     st, ed = 간선
#     arr[st].append(ed)
#     arr[ed].append(st)
# visited = [0] * (정점수 + 1)

# # pprint.pprint(arr)

# res = 0


# def bfs(arr, visited, v):
#     큐 = deque([])
#     큐.append(v)
#     while 큐:
#         정점 = 큐.popleft()
#         visited[정점] = 1
#         for i in range(len(arr[정점])):
#             if visited[arr[정점][i]] == 0:
#                 큐.append(arr[정점][i])


# for i in range(1, 정점수 + 1):
#     if visited[i] == 0:
#         bfs(arr, visited, i)
#         # print(visited)
#         res += 1

# print(res)
