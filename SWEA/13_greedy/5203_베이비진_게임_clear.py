import sys
sys.stdin = open('5203.txt', 'r')

T = int(input())

for tc in range(1, 1 + T):
    deck = list(map(int, input().split()))

    def check(cards):
        for i in range(len(cards)):     # triplet
            if cards.count(i) >= 3:
                return 'win'
        for i in range(len(cards)):     # run
            if cards[i]+1 in cards and cards[i]+2 in cards:
                return 'win'
        return 'not win'
    p1 = []
    p2 = []
    cnt = 0
    res = 0
    for i in range(12):
        if res != 0:
            break
        if i % 2 == 0:
            p1.append(deck[i])
            cnt += 1
            if cnt >= 3:
                if check(p1) == 'win':
                    res = 1
        else:
            p2.append(deck[i])
            if cnt >= 3:
                if check(p2) == 'win':
                    res = 2

    # print(p1, p2)
    print(f'#{tc} {res}')

###
# 명균's


def check(p, idx):  # 아예 카드 갯수를 리스트로 갖다준 방식
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
