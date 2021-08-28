import sys

sys.stdin = open("개념_DFS.txt", "r")
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

# 준비할 것: 인접 행렬 판, 그걸로 완성한 인접 행렬, 시작 정점을 담은 스택, 방문 배열

# 입력 먼저
V, E = map(int, input().split())    # 정점수, 간선수

arr = [[0] * (V + 1) for _ in range(V + 1)]     # (1) 인접행렬 생성 준비
# 한 칸 더 크게 만드는 이유는 인덱스를 맞추어 주기 위해서
# 0번 인덱스따위 버려버리기

for i in range(E):
    st, ed = map(int, input().split())  # 연결 된 두 정점
    arr[st][ed] = arr[ed][st] = 1       # (2) 인접행렬 만들었덩

visited = []        # 방문배열
stack = []          # 스택
stack.append(1)     # 시작 정점을 담는다.

while len(stack) > 0:   # 스택이 빌때까지 무한히 반복
    v = stack.pop()     # 정점을 하나 꺼낸다.
    if v not in visited:    # 해당 정점이 방문한 정점이 아니라면
        print(v, end=" ")
        visited.append(v)   # 정점을 방문체크
        # 현재 정점에서 연결되어있는 모든 정점을 탐색하기 위한 반복문
        for i in range(1, V+1):
            # 현재정점과 연결되어있으면서 방문하지 않은 정점 i가 있다면
            if arr[v][i] == 1 and i not in visited:
                # 모두 다 스택에 push
                stack.append(i)
