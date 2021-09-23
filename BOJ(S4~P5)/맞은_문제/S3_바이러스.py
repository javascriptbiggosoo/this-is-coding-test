# BFS로도 풀어보자

ans = 0


def dfs(v):
    global ans
    visited[v] = 1
    for i in graph[v]:
        if visited[i] != 1:
            ans += 1
            dfs(i)


컴퓨터수 = int(input())
간선수 = int(input())

graph = [[] for _ in range(컴퓨터수 + 1)]  # 첫칸은 안씁니당
for i in range(간선수):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)

visited = [0] * (컴퓨터수 + 1)


dfs(1)
print(ans)
