# 해설안본 상태로 맞춤, 쉬움, 코드 개선점 있음

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

no1 = max(arr)
for i in range(N):
    if arr[i] == no1:
        arr.pop(i)
        break

no2 = max(arr)
count = 0
ans = 0

for _ in range(M):
    if count == K:
        ans += no2
        count = 0
    else:
        ans += no1
        count += 1

print(ans)

# sort()를 이용해서 간단하게 풀어봄
# N, M, K = map(int, input().split())
# arr = list(map(int, input().split()))

# arr.sort()
# no1 = arr.pop()
# no2 = arr.pop()

# 덩어리 = M // (K + 1)
# 꼬다리 = M % (K + 1)
# res = (no1 * K + no2) * 덩어리 + 꼬다리 * no1
# print(res, 덩어리, 꼬다리)