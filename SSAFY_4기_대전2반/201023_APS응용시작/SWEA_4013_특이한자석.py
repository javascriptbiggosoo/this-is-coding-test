def rotate(idx, d):
    if d == 1:  # 시계방향으로 돌릴때
        magnet[idx].insert(0, magnet[idx].pop())
    else:  # 반시계라면
        magnet[idx].append(magnet[idx].pop(0))


def func(idx, d):
    check[idx] = 1

    # 오른쪽 자석을 돌릴 수 있다면
    if idx < 4 and magnet[idx][2] != magnet[idx + 1][6] and not check[idx + 1]:
        func(idx + 1, -d)
    # 왼쪽 자석을 돌릴수 있다면
    if idx > 1 and magnet[idx][6] != magnet[idx - 1][2] and not check[idx - 1]:
        func(idx - 1, -d)

    rotate(idx, d)


for tc in range(1, int(input()) + 1):
    K = int(input())  # 회전수 입력
    ans = 0
    # 0번인덱스를 사용하지 않음
    magnet = [[0]] + [list(map(int, input().split())) for _ in range(4)]

    for i in range(K):
        idx, d = map(int, input().split())  # 몇번 자석을 어디방향으로?

        # 자석이 돌았는지를 체크하는 리스트

        check = [0] * 5
        func(idx, d)

    # 위의 값이 S라면 더하기
    for i in range(4):
        if magnet[i + 1][0]:
            ans += 1 << i

    print("#{} {}".format(tc, ans))
