# 2트 성공, 전역변수 갖다쓰는데에 있어 애로사항이 있었음 주석 참고

# 1트, 손도 못댔으니 손댔으면 당연 틀림, 일단 완전탐색해도 된다는 판단 자체를 못했고
# 최적의 풀이를 계속 고민했는데, 완전탐색이면 충분한 문제였다.
# 그리고 알고 난 이후에도 조합을 구현하는데 있어 어려움이 느껴졌음.


# https://www.acmicpc.net/problem/14502
import pprint

세로, 가로 = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(세로)]
# pprint.pprint(arr)
arr_visited = [[0] * 가로 for _ in range(세로)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

res = 0


# 벽 세우기 완전탐색(조합..)
def virus(r, c):
    arr_visited[r][c] = 2
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 세로 and 0 <= nc < 가로 and arr[nr][nc] != 1 and arr_visited[nr][nc] == 0:
            virus(nr, nc)


# 그 중 안전영역 제일 큰 값을 저장해두기
def safe_checker():
    dan = 0
    for i in range(세로):
        for j in range(가로):
            if arr[i][j] == 1:
                dan += 1
            if arr_visited[i][j] == 2:
                dan += 1
    safe_zone = 세로 * 가로 - dan
    return safe_zone


# 완전탐색 순간마다 dfs돌리기


def dfs(cnt):
    global res, arr_visited  # <<<
    # 벽 세개 세워졌을 때 안전영역 체크,
    if cnt == 3:
        for i in range(세로):
            for j in range(가로):
                if arr[i][j] == 2:
                    virus(i, j)
                    # pprint.pprint(arr_visited)
        res = max(res, safe_checker())
        arr_visited = [
            [0] * 가로 for _ in range(세로)
        ]  # <<< 밖에 있던 전역변수를 함수 내에서 재선언하면, 함수에서 애초부터 전역변수를 받지 않는다. 처음에 전역에서 한 번 받아올 필요가 있기 때문에 이 코드에선 전역으로 global arr_visited로 전역변수 등록을 해주어야한다.
        return
    for i in range(세로):
        for j in range(가로):
            if arr[i][j] == 0:
                cnt += 1
                arr[i][j] = 1
                dfs(cnt)
                cnt -= 1
                arr[i][j] = 0


dfs(0)
print(res)
