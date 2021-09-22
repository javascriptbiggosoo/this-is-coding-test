ans = 0


# def dfs(v):


컴퓨터수 = int(input())
간선수 = int(input())

graph = [[] for _ in range(컴퓨터수 + 1)]  # 첫칸은 안씁니당
print(graph)
for i in range(간선수):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)

visited = [0] * (컴퓨터수 + 1)
print(graph)

# dfs(1)
print(ans)
