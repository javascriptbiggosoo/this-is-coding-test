# https://www.acmicpc.net/problem/14503
# 1트, 1시간 넘게 걸림, 주석 참조
# from pprint import pprint as pp

n, m = map(int, input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


cnt = 0  # 답
추진력 = 0
while True:
    # 현재 위치를 청소한다.
    if arr[r][c] == 0:
        arr[r][c] = 2 + cnt
        cnt += 1
        추진력 = 0  # <<<<<<<<<<<<<<<<<< 이거 안해주는 것 땜에 한참 헤맴
        # pp(arr)
    # 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
    d = (d - 1) % 4
    nr = r + dr[d]
    nc = c + dc[d]
    # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    if arr[nr][nc] == 0:
        r = nr
        c = nc
        continue
    # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    else:
        추진력 += 1
        # 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        if 추진력 == 4:
            추진력 = 0
            nr = r - dr[d]
            nc = c - dc[d]
            # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
            if arr[nr][nc] != 1:
                r = nr
                c = nc
            else:
                break

print(cnt)
