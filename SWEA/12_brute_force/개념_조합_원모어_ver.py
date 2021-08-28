def f(n, s, N, r):  # c[n]의 조합의 인덱스, 선택구간시작, 총 갯수, 고를 갯수
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
