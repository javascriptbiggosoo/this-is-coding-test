from collections import deque

n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]
# print(arr)

큐 = deque(arr)

ans = []
while len(큐):
    for i in range(k - 1):
        큐.append(큐.popleft())
    ans.append(큐.popleft())

print("<", end="")
for i in range(n - 1):
    print(str(ans[i]) + ", ", end="")
print(ans[-1], end="")
print(">")
