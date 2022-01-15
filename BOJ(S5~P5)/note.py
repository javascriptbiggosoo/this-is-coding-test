from collections import deque


def bfs(arr, v, visited):
    q = deque([])
    visited[v] = True
    q.append(arr[v])
    print(v, end=" ")
    while q:
        curr = q.popleft()
        for i in curr:
            if visited[i] is False:
                q.append(arr[i])
                print(i, end=" ")
                visited[i] = True


def dfs(arr, v, visited):
    print(v, end=" ")
    visited[v] = True
    for i in arr[v]:
        if visited[i] is False:
            dfs(arr, i, visited)


정점수, 간선수, 시작점 = map(int, input().split())
인접리스트 = [[] for _ in range(정점수 + 1)]
visited = [False] * (정점수 + 1)

for i in range(간선수):
    st, ed = map(int, input().split())
    인접리스트[st].append(ed)
    인접리스트[ed].append(st)

# dfs(인접리스트, 시작점, visited)
print()
bfs(인접리스트, 시작점, visited)
