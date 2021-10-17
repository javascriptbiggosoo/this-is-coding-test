# # 뱀 푸는 중
# # 뱀 푸는 중
# # 뱀 푸는 중

# import sys, pprint

# n = int(sys.stdin.readline().rstrip())

# arr = [[0] * (n + 1) for _ in range(n)]


# k = int(sys.stdin.readline().rstrip())

# for i in range(k):
#     row, col = map(int, sys.stdin.readline().rstrip().split())
#     arr[row][col] = 1

# pprint.pprint(arr)
# l = int(sys.stdin.readline().rstrip())

# for i in range(l):
#     time, ctrl = sys.stdin.readline().rstrip().split()
#     time = int(time)
from collections import deque
import pprint


def dfs(arr, v, visited):
    visited[v] = 1
    print(v)
    for i in range(len(arr[v])):
        if visited[arr[v][i]] == 0:
            dfs(arr, arr[v][i], visited)


정점수, 간선수, 시작점 = map(int, input().split())

정점들 = [[] for _ in range(정점수 + 1)]
visited = [0] * (정점수 + 1)
for i in range(간선수):
    st, ed = map(int, input().split())
    정점들[st].append(ed)
    정점들[ed].append(st)

dfs(정점들, 시작점, visited)
