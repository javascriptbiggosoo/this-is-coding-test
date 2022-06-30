import sys

sys.stdin = open("5247_input.txt", "r")

from collections import deque


def bfs():
    queue = deque()
    queue.append(N)

    ans = 0
    while queue:
        size = len(queue)

        for i in range(size):
            curr = queue.popleft()
            if curr == M: return ans
            for j in (curr + 1, curr - 1, curr * 2, curr - 10):
                if 0 < j <= 1000000 and memo[j] == -1:
                    memo[j] = 1
                    queue.append(j)
        ans += 1


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    memo = [-1] * 1000001
    print("#{} {}".format(tc, bfs()))

######################################################3
#2번
def calc(num, idx):
    if idx == 0:
        return num + 1
    elif idx == 1:
        return num - 1
    elif idx == 2:
        return num * 2
    else:
        return num - 10


def bfs():
    queue = [0] * 1000000
    front = rear = -1
    rear += 1
    queue[rear] = N
    while front != rear:
        front += 1
        curr_N = queue[front]
        if curr_N == M:
            return
        for i in range(4):
            next_N = calc(curr_N, i)
            if 0 < next_N <= 1000000 and memo[next_N] == -1:
                memo[next_N] = memo[curr_N]+1
                rear += 1
                queue[rear] = next_N


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    memo = [-1] * 1000001
    memo[N] = 0
    bfs()
    print("#{} {}".format(tc, memo[M]))
#####################################################

###########################################################
#1번
def calc(num, idx):
    if idx == 0:
        return num + 1
    elif idx == 1:
        return num - 1
    elif idx == 2:
        return num * 2
    else:
        return num - 10


def bfs():
    queue = [0] * 1000000
    front = rear = -1
    rear += 1
    queue[rear] = (N, 0)
    while front != rear:
        front += 1
        curr_N, curr_cnt = queue[front]
        if curr_N == M:
            return curr_cnt
        for i in range(4):
            next_N = calc(curr_N, i)
            if 0 < next_N <= 1000000:
                rear += 1
                queue[rear] = (next_N, curr_cnt + 1)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    print("#{} {}".format(tc,bfs()))