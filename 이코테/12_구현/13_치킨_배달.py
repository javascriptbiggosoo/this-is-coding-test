# https://www.acmicpc.net/problem/15686

n, m = map(int, input().split())
도시 = [list(map(int, input().split())) for _ in range(n)]
print(도시)

home = []
chicken = []
for row in range(n):
    for col in range(n):
        if 도시[row][col] == 1:
            home.append([row, col])
        elif 도시[row][col] == 2:
            chicken.append([row, col])


cnt = 0


# 1. M개의 치킨집이 생길 수 있는 모든 경우를 구한다(조합? DFS?)
while True:

    if cnt == m:
        # 2. 각 경우의 치킨거리 합을 구한다
        break
        # 3. 그 중 최소인 치킨거리를 저장한다
    cnt += 1
