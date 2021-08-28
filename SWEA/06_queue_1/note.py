import sys

sys.stdin = open("개념_BFS.txt", "r")


def BFS(v):
    visited[v] = 1
    queue = []
    queue.append(v)
    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr, end=' ')
        for i in adj_arr[curr]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


V, E = map(int, input().split())
adj_arr = [[] for _ in range(V+1)]

for i in range(E):
    st, ed = map(int, input().split())
    adj_arr[st].append(ed)
    adj_arr[ed].append(st)
visited = [0] * (V+1)

BFS(1)