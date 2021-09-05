# 1트
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

정답 = 0

for i in range(n):
    if 정답 < min(arr[i]):
        정답 = min(arr[i])

print(정답)
