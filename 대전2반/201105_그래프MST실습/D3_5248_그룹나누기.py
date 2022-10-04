def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    # p = [0] * (V + 1)
    # for i in range(V + 1):
    #     make_set(i)
    p = list(range(V+1))
    edge = list(map(int, input().split()))
    for i in range(E):
        st = edge[i * 2]
        ed = edge[i * 2 + 1]
        union(st, ed)

    #이거 안쓰면 어떻게 되는지 보여주기
    for i in range(1, V + 1):
        find_set(i)

    #0도 들어있으니까
    print("#{} {}".format(tc, len(set(p)) - 1))


####################################################
def bfs(st):
    queue = [st]
    team[st] = True
    while queue:
        cur = queue.pop(0)
        for i in range(1, V + 1):
            if not team[i] and adj[cur][i] == 1:
                team[i] = True
                queue.append(i)


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]

    edge = list(map(int, input().split()))
    team = [False] * (V + 1)
    # for i in range(0, len(edge), 2):
    #     st = edge[i]
    #     ed = edge[i+1]
    #
    for i in range(E):
        st = edge[i * 2]
        ed = edge[i * 2 + 1]
        adj[st][ed] = adj[ed][st] = 1

    ans = 0
    for i in range(1, V + 1):
        if not team[i]:
            # team[i] = True
            ans += 1
            bfs(i)

    print("#{} {}".format(tc, ans))
