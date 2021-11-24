# https://www.acmicpc.net/problem/9095

T = int(input())


d = [0] * 1234
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, 12):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for tc in range(T):
    n = int(input())
    print(d[n])
