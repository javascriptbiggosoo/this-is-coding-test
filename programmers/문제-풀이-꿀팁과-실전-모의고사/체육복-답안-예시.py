def solution(n, lost, reserve):
    u = [1] * (n + 2)  # 인덱스 에러 방지용 양 끝 벽 뒤에 공간있어요
    # 이렇게 안하고 범위를 한 칸씩 좁힌 후 예외 2가지를 추가하는 방식도 있지만 그건 너무 하수같자너

    for i in reserve:
        u[i] += 1

    for i in lost:
        u[i] -= 1

    for i in range(1, n + 1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i - 1 : i + 1] = [1, 1]  # 생소한 작성법이다.
        elif u[i] == 2 and u[i + 1] == 0:
            u[i : i + 2] = [1, 1]

    return len([x for x in u[1:-1] if x > 0])  # 이건 그냥 n에서 0카운트한걸 빼도 될듯
