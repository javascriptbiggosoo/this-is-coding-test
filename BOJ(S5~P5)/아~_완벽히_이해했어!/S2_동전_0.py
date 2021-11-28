N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
res = 0
for i in range(N):
    curr = arr[N - 1 - i]
    if curr > K:
        continue
    res += K // curr
    K = K % curr
    if K <= 0:
        break
print(res)
