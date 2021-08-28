# 큐로 푼건 아닌..
import sys
sys.stdin = open("5097.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    # 12345 : (index)12012
    M = M % N
    res = seq[M]
    if M == N:
        res = seq[0]

    print('#{} {}'.format(tc, res))
