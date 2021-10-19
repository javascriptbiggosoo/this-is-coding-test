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
import sys, pprint
from collections import deque

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


def bfs(arr, visited, v):
    큐 = deque([])
    큐.append(v)
    while 큐:
        정점 = 큐.popleft()
        visited[정점] = 1
        for i in range(len(arr[정점])):
            if visited[arr[정점][i]] == 0:
                큐.append(arr[정점][i])


for i in range(1, 정점수 + 1):
    if visited[i] == 0:
        bfs(arr, visited, i)
        # print(visited)
        res += 1

print(res)
