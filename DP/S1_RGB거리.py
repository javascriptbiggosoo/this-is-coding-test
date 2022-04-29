# 도저히 혼자 1트로 못풀어서 고민끝에 구글링으로 힌트를 얻음
# 이 문제는 여태껏 dp에서 하나씩만 d에 넣은것과 다르게 값을 3개씩 넣어야함
# 가장 나중에 추가되는 값이 무엇이냐에 따라 계속 앞으로 거슬러 가야하기 때문에
# 회차별로 거슬러 가는 것 보다 모든 경우를 미리 따져놓는게 이득
# https://www.acmicpc.net/problem/1149

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

d = [[0, 0, 0]]

for i in range(n):
    d1 = min(d[i][1], d[i][2]) + arr[i][0]
    d2 = min(d[i][0], d[i][2]) + arr[i][1]
    d3 = min(d[i][1], d[i][0]) + arr[i][2]
    d.append([d1, d2, d3])

print(min(d[-1]))
