def f(n, s, N, r):  # n c[n]의 조합의 인덱수 , s선택구간시작, N주어진개수, r 고를개수
    if n == r:
        print(c)
        return

    for i in range(s, N - r + n + 1):
        c[n] = i
        f(n + 1, i + 1, N, r)


N = 6
r = 3
c = [0] * 3

f(0, 0, N, r)
