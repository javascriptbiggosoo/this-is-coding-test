# 1트 성공, 구현 자잘한 실수땜에 좀 오래 걸리긴 했음;
# bfs기 때문에 방문한적을 없는 곳을 방문했다? 그게 무조건 최소임 그대로 박아넣으면됨
from collections import deque


arr = [0] * (1000001)
n, k = map(int, input().split())


def ec(x):
    return [x - 1, x + 1, x * 2]


def bfs():
    큐 = deque([])
    큐.append(n)
    while len(큐):
        x = 큐.popleft()
        if x == k:
            print(arr[k])
            break
        for nx in ec(x):
            if 0 <= nx < 1000001 and not arr[nx]:
                arr[nx] = arr[x] + 1
                큐.append(nx)


# 동생이 뒤에 있으면 그냥 숫자 차이가 답
if k <= n:
    print(n - k)
# 동생이 앞에 있을 때가 문제
else:
    bfs()
