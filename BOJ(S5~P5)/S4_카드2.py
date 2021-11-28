from collections import deque

n = int(input())
arr = []
for i in range(1, n + 1):
    arr.append(i)

큐 = deque(arr)

while len(큐) > 2:
    큐.popleft()
    큐.append(큐.popleft())

print(큐.pop())
