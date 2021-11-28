# 2트, combinations 사용법을 익혀두자
# https://www.acmicpc.net/problem/15686
from itertools import combinations


n, m = map(int, input().split())
도시 = [list(map(int, input().split())) for _ in range(n)]
# print(도시)

home = []
chicken = []
for row in range(n):
    for col in range(n):
        if 도시[row][col] == 1:
            home.append([row, col])
        elif 도시[row][col] == 2:
            chicken.append([row, col])


# 1. M개의 치킨집이 생길 수 있는 모든 경우를 구한다(조합? DFS?)
후보들 = list(combinations(chicken, m))

ans = 987654321


def 치킨거리(후보):
    ans = 0
    for r, c in home:
        이집 = []
        for row, col in 후보:  # m개의 후보
            이집.append(abs(r - row) + abs(c - col))
        # 3. 그 중 최소인 치킨거리를 저장한다
        ans += min(이집)
    return ans


# 2. 각 경우의 치킨거리 합을 구한다
for 후보 in 후보들:
    ans = min(ans, 치킨거리(후보))

print(ans)

# # 1트, M개 조합을 어떻게 구현할지 막막해서 손을 못댔다.
# n, m = map(int, input().split())
# 도시 = [list(map(int, input().split())) for _ in range(n)]
# print(도시)

# home = []
# chicken = []
# for row in range(n):
#     for col in range(n):
#         if 도시[row][col] == 1:
#             home.append([row, col])
#         elif 도시[row][col] == 2:
#             chicken.append([row, col])


# cnt = 0


# # 1. M개의 치킨집이 생길 수 있는 모든 경우를 구한다(조합? DFS?)
# while True:

#     if cnt == m:
#         # 2. 각 경우의 치킨거리 합을 구한다
#         break
#         # 3. 그 중 최소인 치킨거리를 저장한다
#     cnt += 1
