도시개수 = int(input())
도시간거리 = list(map(int, input().split()))
도시별유가 = list(map(int, input().split()))

최저가 = min(도시별유가)
현재도시 = 0
최소비용 = 0

while True:
    if 도시별유가[현재도시] == 최저가:
        최소비용 += 최저가 * 도시간거리[현재도시:]
        break
    else:
        for 도시 in range(현재도시+1, 도시개수):
            