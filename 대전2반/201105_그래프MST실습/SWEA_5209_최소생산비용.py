def check(visited, idx, result):
    global ans

    # 가지치기
    if result > ans:
        return

    if visited == (1 << N) - 1:
        ans = min(ans, result)
        return

    for i in range(N):
        if visited & (1 << i): continue
        check(visited | 1 << i, idx + 1, result + cost[idx][i])


for tc in range(1, int(input()) + 1):
    N = int(input())

    cost = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321
    # 첫번째 제품을 모든공장에서 만들어 보고 출발시킴
    # 제품이 5개라면
    # 00001
    # 00010
    # 00100
    # 01000
    # 10000
    for i in range(N):
        check(1 << i, 1, cost[0][i])

    print("#{} {}".format(tc, ans))
