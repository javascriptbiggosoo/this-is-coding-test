# https://www.acmicpc.net/problem/18352
import sys
from collections import deque

도시수, 도로수, 타겟, 출발점 = map(int, sys.stdin.readline().rstrip().split())

# 인접 리스트
arr = [[] for _ in range(도시수 + 1)]
visited = [0 for _ in range(도시수 + 1)]

res = []


def bfs(v):
    q = deque([[v, 0]])  # 시작점, 최단거리
    visited[v] = 1  # 방문 체크
    while q:
        v, dst = q.popleft()
        if dst == 타겟:
            res.append(v)
        for i in arr[v]:
            if visited[i] == 0:
                q.append([i, dst + 1])
                visited[i] = 1


for i in range(도로수):
    st, ed = map(int, sys.stdin.readline().rstrip().split())
    arr[st].append(ed)

bfs(출발점)
if res:
    for i in sorted(res):
        print(i)
else:
    print(-1)
