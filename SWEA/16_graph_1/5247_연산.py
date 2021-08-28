import sys
sys.stdin = open('5247.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())

    cnt_m2 = 0
    m2 = N
    m2s = [N]
    while m2 <= M:
        m2 *= 2
        m2s.append(m2)
        cnt_m2 += 1
    print(cnt_m2)
    print(m2s)
    un_m2 = m2//2
    print(un_m2)

