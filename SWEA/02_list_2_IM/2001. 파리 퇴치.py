# 0904 문제풀이

import sys

sys.stdin = open("2001.txt", "r")


def check(row, col):
    tsum = 0
    # for r in range(row, row + M):         # 같은
    for r in range(M):
        # for c in range(col, col + M):     # 표현
        for c in range(M):
            # total += fly[r][c]            # 이다
            tsum += arr[row + r][col + c]


    return tsum


T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for r in range(N - M + 1):      # 설마 4중 for문? 와.. 맞았어..
        for c in range(N - M + 1):  # 큰덩어리 2차원탐색, 작은덩어리 2차원 탐색
            tmp = check(r, c)       # 자력 풀이 1회차때 이부분 이하3 줄이 안떠오름
            if ans < tmp:
                ans = tmp
            # ans = max(ans , tmp)  # if 부분을 이렇게 할 수도 있다

    print('#{} {}'.format(tc, ans))


