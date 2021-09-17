n = int(input())
거리 = list(map(int, input().split()))
주유가 = list(map(int, input().split()))

최저가 = min(주유가)
현재도시 = 0
ans = 0
while True:
    # 제일 싼 곳에 도착했으면 여기서 풀충전한다.
    if 주유가[현재도시] == 최저가:
        ans += 주유가[현재도시] * sum(거리[현재도시:])
        break
    # 현재보다 싼 곳이면 그까지 가서 충전한다.
    for i in range(현재도시 + 1, n):
        if 주유가[현재도시] > 주유가[i]:
            ans += 주유가[현재도시] * sum(거리[현재도시:i])
            현재도시 = i
            break
print(ans)
