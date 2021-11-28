# 2트 성공, sys.setrecursionlimit(10000).. 이거 써서 맞추니까 왠지 비겁한 느낌인데 하여튼 맞춤

# 1트 성공(아님), 이제 요런건 쉽다 ㅎㅎㅎㅎㅎㅎㅎ 비슷한 유형 많이 푸러봤음 이라고 생각했는데 dfs 런타임 에러가 나버리네
# 아 ㅋㅋ bfs 로 즉시 수정
# 했는데 이번엔 또 시간초과에 메모리초과.. 걸림 하.. 뭐지
from collections import deque
import sys

sys.setrecursionlimit(10000)

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 1, -1, 0, 1, -1, 0]


def dfs(arr, r, c):
    arr[r][c] = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1:
            dfs(arr, nr, nc)


# def bfs(arr, r, c):
#     q = deque([[r, c]])
#     while q:
#         r, c = q.popleft()
#         arr[r][c] = 0
#         for i in range(8):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1:
#                 q.append([nr, nc])


while True:  # 각 tc마다 실행
    res = 0
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if arr[r][c] == 1:
                # bfs(arr, r, c)
                dfs(arr, r, c)
                res += 1
    print(res)
