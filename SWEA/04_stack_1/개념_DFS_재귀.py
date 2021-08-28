# 이걸 완벽히 이해했다면 역으로 V-1들을 V로 바꿔보자. 빨리 해낸다면 이해가 된 것이겠지?

import sys

sys.stdin = open("개념_DFS.txt", "r")
# 그래프를 보고 각 정점의 번호를 출력해봅시다.
# 7 8   # 정점수, 간선수
# 1 2   # 여기부터는 연결되어 있는 두 정점
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7


def DFS(v):
    print(v, end=" ")
    # 방문체크
    visited[v] = 1
    for i in range(1, V + 1):   # 한 행(i에 해당하는 정점의 인접행렬)을 돌면서 인접행렬에서 값이 1이고! 방문배열에서 값이 0이라면! 똑똑, 방문하겠습니다 ㅎㅎ
        if arr[v][i] == 1 and visited[i] == 0:  # 1을 시작정점으로 했을 경우, 이 if문은 반복문 내에서 2와 3일 때만 작동한다 근데 3일땐 작동을 해도 그 내부에서 이미 3과 연결된 1과 7을 방문했기에 여기선 의미가 없지만!
            DFS(i)


V, E = map(int, input().split())
# 인접행렬 생성 준비
arr = [[0] * (V + 1) for _ in range(V + 1)]     # 0번 안쓸건데 한 칸 더 만드는 이유는 인덱스를 맞추어 주기 위해서 V + 1


for i in range(E):
    st, ed = map(int, input().split())  # 서로 연결돼 있음을 표시
    arr[st][ed] = arr[ed][st] = 1

# 방문 배열 선언
visited = [0] * (V + 1)

DFS(1)
