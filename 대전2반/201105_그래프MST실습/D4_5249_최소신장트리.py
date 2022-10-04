import sys

sys.stdin = open("5249_input.txt", "r")

import heapq


def MST_PRIM():
    visited = [False] * (V + 1)

    heap = []
    # 가중치와 점
    heapq.heappush(heap, (0, 0))
    ans = 0
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = True

            for idx, weight in adj[v]:
                if not visited[idx]:
                    heapq.heappush(heap, (weight, idx))

    return ans


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    # 임의의 큰값으로 초기화된 값을 넣는다.
    adj = [[] for _ in range(V + 1)]
    for i in range(E):
        st, ed, weight = map(int, input().split())
        adj[st].append((ed, weight))
        adj[ed].append((st, weight))

    print("#{} {}".format(tc, MST_PRIM()))
##############################################################
def MST_PRIM():
    global ans
    key = [987654321] * (V + 1)
    # p = [None] * (V + 1)
    visited = [False] * (V + 1)
    key[0] = 0

    for _ in range(V):
        # 최솟값찾기
        minIdx = -1
        min = 987654321
        for i in range(V + 1):
            if not visited[i] and key[i] < min:
                min = key[i]
                minIdx = i
        visited[minIdx] = True
        # 갱신가능하면 갱신
        for i in range(V + 1):
            if not visited[i] and adj[minIdx][i] < key[i]:
                key[i] = adj[minIdx][i]
                # p[i] = minIdx

    for i in range(V + 1):
        ans += key[i]


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 임의의 큰값으로 초기화된 값을 넣는다.
    adj = [[987654321] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        st, ed, weight = map(int, input().split())
        adj[st][ed] = adj[ed][st] = weight
    ans = 0

    MST_PRIM()

    print("#{} {}".format(tc, ans))


###############################################
def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union_set(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(E)]
    p = [0] * (V + 1)
    edges = sorted(edges, key=lambda x: x[2])
    for i in range(V + 1):
        make_set(i)

    ans = 0
    cnt = 0  # 간선수  0부터 시작했으므로 V개 뽑
    idx = 0  #
    while cnt < V:
        x = edges[idx][0]
        y = edges[idx][1]
        if find_set(x) != find_set(y):
            union_set(x, y)
            cnt += 1
            ans += edges[idx][2]
        idx += 1

    print("#{} {}".format(tc, ans))
