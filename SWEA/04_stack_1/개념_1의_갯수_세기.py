import sys

sys.stdin = open("개념_1의_갯수_세기.txt", "r")
# input
# 7(정사각형)
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000
#
# output: 2 13 (덩어리 당 1의 갯수)

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(r, c):
    # 개수를 위한 글로벌 선언
    global cnt
    # 요기 왔다는건 1이라는 뜻이므로 카운트 증가
    arr[r][c] = 0   # DFS 돌린 것은 for문에서 다시 돌지 않도록
    # 이거 함수 밖에서도 적용됨
    cnt += 1
    for i in range(4):  # 에너미 컨트롤러!
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위를 벗어나면 out, 다음좌표가 0이라면 out
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[nr][nc] == 0:
            continue
        # 위에 다걸리지 않았다면 다음 좌표도 1이고 맵의 크기도 안벗어난 것이므로 재귀
        DFS(nr, nc)

        # 이건 note.py에다가 내가 친 코드인데 위는 안되고 아래는 됨; 위로 치고 뭐가 문젠지 30분 봄. 진기명기 ㅋㅋㅋㅋㅋ
        # if arr[nr][nc] == 1 and width > nr >= 0 and width > nc >= 0:

        # if width > nr >= 0 and width > nc >= 0 and arr[nr][nc] == 1:
        #     DFS(nr, nc)



N = int(input())    # (1)

arr = [list(map(int, input())) for _ in range(N)]   # (2)
print(arr)
for i in range(N):      # (3)
    for j in range(N):  # 배열의 각 칸마다 조회 하겄으
        if arr[i][j] == 1:  # 1이여?
            cnt = 0
            DFS(i, j)       # DFS 돌려
            print(cnt)
