# 해설안본 상태로 맞춤, 쉬움, 코드 개선점 있음

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

max_num = max(arr)
for i in range(N):
    if arr[i] == max_num:
        arr.pop(i)
        break

second_num = max(arr)
count = 0
ans = 0

for _ in range(M):
    if count == K:
        ans += second_num
        count = 0
    else:
        ans += max_num
        count += 1

print(ans)
