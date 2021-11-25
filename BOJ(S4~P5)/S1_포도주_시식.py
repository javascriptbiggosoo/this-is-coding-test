# https://www.acmicpc.net/problem/2156

n = int(input())

d = [0] * 10001  # 각 회차당 최대
di = [0] * 10001  # 각 회차의 인풋
d[1] = int(input())
di[1] = d[1]
if n > 1:
    di[2] = int(input())
    d[2] = d[1] + di[2]
    if n > 2:
        di[3] = int(input())
        d[3] = max(d[2], d[1] + di[3], d[2] - d[1] + di[3])
        if n > 3:
            for i in range(4, n + 1):
                di[i] = int(input())
                d[i] = max(d[i - 1], d[i - 2] + di[i], d[i - 3] + di[i] + di[i - 1])

print(d[n])
