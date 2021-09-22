def dfs(v):
    print(v, end=" ")
    visited[v] = 1
    for i in graph[v]:
        if visited[i] != 1:
            dfs(i)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [0] * 9
dfs(1)
print(visited)
