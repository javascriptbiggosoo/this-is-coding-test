# 순서 주어지는 큐랑 우선순위큐 같이 만듬
from collections import deque


t = int(input())

for tc in range(t):

    갯수, 타겟 = map(int, input().split())

    순번 = []
    for i in range(갯수):
        순번.append(i)
    순번 = deque(순번)

    큐 = deque(map(int, input().split()))
    # print(큐, 순번)
    ans = 0
    while 타겟 in 순번:

        if 큐[0] == max(큐):
            큐.popleft()
            순번.popleft()
            ans += 1
        else:
            큐.append(큐.popleft())
            순번.append(순번.popleft())
        # print(큐)
    print(ans)
