def check(p, idx):
    if p[idx] >= 3:
        return True

    # run
    for i in range(1, 9):
        if p[i - 1] and p[i] and p[i + 1]:
            return True

    return False


for tc in range(1, int(input()) + 1):
    card = list(map(int, input().split()))  # 카드입력
    player1 = [0] * 10
    player2 = [0] * 10

    win = 0

    for i in range(0, len(card), 2):
        player1[card[i]] += 1
        player2[card[i + 1]] += 1

        flag1 = check(player1, card[i])
        flag2 = check(player2, card[i + 1])

        if flag1:
            win = 1
            break
        elif flag2:
            win = 2
            break

    print("#{} {}".format(tc, win))
