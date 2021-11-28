# 1트 성공, 근데 bfs가 익숙하지 않아서 여러번 고쳤음. 연습 더 하자.
from collections import deque
# import pprint


def dfs(인접행렬, 방문, 시작점):
    print(시작점, end=" ")
    방문[시작점] = 1
    for i in range(1, len(인접행렬)):
        if 인접행렬[시작점][i] == 1 and 방문[i] == 0:
            dfs(인접행렬, 방문, i)


def bfs(인접행렬, 방문, 시작점):
    방문[시작점] = 1
    큐 = deque([시작점])
    print(시작점, end=" ")
    while 큐:
        정점 = 큐.popleft()
        for i in range(1, len(인접행렬)):
            if 인접행렬[정점][i] == 1 and 방문[i] == 0:
                큐.append(i)
                방문[i] = 1
                print(i, end=" ")


정점수, 간선수, 시작점 = map(int, input().split())

방문 = [0] * (정점수 + 1)
인접행렬 = [[0] * (정점수 + 1) for _ in range(정점수 + 1)]
for i in range(간선수):
    st, ed = map(int, input().split())
    인접행렬[st][ed] = 1
    인접행렬[ed][st] = 1

# pprint.pprint(인접행렬)

# 안보고 다시 풀어본 dfs

# dfs(인접행렬, 방문, 시작점)
# 방문 = [0] * (정점수 + 1)

# print("")
# bfs(인접행렬, 방문, 시작점)

# def dfs(arr, v, visited):
#     visited[v] = 1
#     print(v)
#     for i in range(len(arr[v])):
#         if visited[arr[v][i]] == 0:
#             dfs(arr, arr[v][i], visited)


# 정점수, 간선수, 시작점 = map(int, input().split())

# 인접리스트 = [[] for _ in range(정점수 + 1)]
# 방문 = [0] * (정점수 + 1)
# for i in range(간선수):
#     st, ed = map(int, input().split())
#     인접리스트[st].append(ed)
#     인접리스트[ed].append(st)

# dfs(인접리스트, 시작점, 방문)
