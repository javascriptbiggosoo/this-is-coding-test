def permutaion(idx):
    global ans
    if idx == N + 1:
        total = 0

        for i in range(N + 1):
            total += abs(pos[i][0] - pos[i + 1][1]) + abs(pos[i][1] - pos[i + 1][1])
        ans = min(ans, total)
        return

    for i in range(idx, N + 1):
        pos[i], pos[idx] = pos[idx], pos[i]
        permutaion(idx + 1)
        pos[i], pos[idx] = pos[idx], pos[i]


for tc in range(1, int(input()) + 1):
    N = int(input())

    tmp = list(map(int, input().split()))
    #회사 집 고객 좌표를
    #회사 고객 집 좌표로 바꾸기
    pos = [(tmp[0], tmp[1])]
    for i in range(4, len(tmp), 2):
        pos.append((tmp[i], tmp[i + 1]))
    pos.append((tmp[2], tmp[3]))

    ans = 98765421

    permutaion(1)

    print("#{} {}".format(tc, ans))
