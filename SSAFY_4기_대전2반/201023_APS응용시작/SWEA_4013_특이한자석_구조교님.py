for t in range(int(input())):
    n = int(input())  #회전 수
    a = 0 # 정답
    g = [[*map(int, input().split())] for _ in range(4)] #g 자석 4개 입력

    for _ in range(n):
        i, m = map(int, input().split()) #i는 자석인덱스, m회전방향
        i -= 1 #0번 인덱스부터 활용하기 때문에 -1로 조정
        r = [(i, m)] #나중에 회전

        # 왼쪽으로 이동을 하면서
        p = m
        for j in range(i, 0, -1):
            if g[j - 1][2] != g[j][6]:
                p *= -1;
                r += [(j - 1, p)]
            #차례대로 검사해서 조건에 안맞으면 그이후는 볼필요도 없음
            else:
                break

        # 오른쪽으로 이동을 하면서
        p = m
        for j in range(i + 1, 4):
            if g[j][6] != g[j - 1][2]:
                p *= -1;
                r += [(j, p)]
            else:
                break

        #회전들을 이제 회전시키기
        for i, m in r:
            if m == 1:
                g[i] = [g[i].pop()] + g[i]
            elif m == -1:
                g[i] += [g[i].pop(0)]

    for i in range(4):
        a += g[i][0] * 2 ** i

    print(f'#{t + 1}', a)
