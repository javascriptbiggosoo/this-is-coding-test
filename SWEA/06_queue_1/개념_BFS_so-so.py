import sys

sys.stdin = open("개념_BFS.txt", "r")
# input
# 7 8   # 정점수, 간선수
# 1 2   # 여기부터는 연결되어 있는 두 정점
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7
# queue: 줄세워서 실제로 꺼내 쓸 곳 / visited: 중복 방지용으로 체크 / curr: 쓸모를 다 하고 버릴 친구 ㅠㅠ


def BFS(a):
    queue = []
    queue.append(a)     # 시작점을 큐에 넣어봐요
    visited[a] = 1      # 시작점 방문 기록~

    while len(queue) > 0:       # 큐가 비는 순간 멈추므로 끝 층에 도달할 때 멈추는 것
        curr = queue.pop(0)
        '''
        curr = queue.pop()
        이 코드로 하면 하나씩 돌긴 하지만 queue는 아니다.
        출력은 1 3 7 6 5 4 2로 나온다~~
        '''
        print(curr, end=' ')    # 출력문

        for i in adj_list[curr]:    # 연결된 점이
            if not visited[i]:      # 방문 안됐다면
                queue.append(i)     # 큐에 처넣어!
                visited[i] = 1      # 아 그리고 방문 기록 남기자 ㅎ


V, E = map(int, input().split())

adj_list = [[] for _ in range(V+1)]     # (1) 인접 리스트

for i in range(E):
    st, ed = map(int, input().split())
    adj_list[st].append(ed)
    adj_list[ed].append(st)

visited = [0] * (V+1)       # 왜 V+1?? 인덱스를 그대로 쓰고 싶어서

BFS(1)
