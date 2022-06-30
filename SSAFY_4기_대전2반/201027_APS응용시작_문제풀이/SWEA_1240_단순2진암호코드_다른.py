P = {(3, 2, 1, 1): 0,
     (2, 2, 2, 1): 1,
     (2, 1, 2, 2): 2,
     (1, 4, 1, 1): 3,
     (1, 1, 3, 2): 4,
     (1, 2, 3, 1): 5,
     (1, 1, 1, 4): 6,
     (1, 3, 1, 2): 7,
     (1, 2, 1, 3): 8,
     (3, 1, 1, 2): 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]


    def find():
        for i in range(N):
            for j in range(M - 1, -1, -1):
                if arr[i][j] == '0': continue
                pwd = []
                idx = j
                for k in range(8):
                    c1 = c2 = c3 = c4 = 0
                    while arr[i][idx] == '1':
                        c4, idx = c4 + 1, idx - 1
                    while arr[i][idx] == '0':
                        c3, idx = c3 + 1, idx - 1
                    while arr[i][idx] == '1':
                        c2, idx = c2 + 1, idx - 1
                    c1= 7 - (c2+c3+c4)

                    pwd.append(P[(c1,c2,c3,c4)])
                    idx -= c1

                a = pwd[0] + pwd[2] + pwd[4] + pwd[6] #짝수합
                b = pwd[1] + pwd[3] + pwd[5] + pwd[7] #홀수합

                if ((b*3)+a)%10 == 0:
                    return a+b
                else:
                    return 0

    print("#{} {}".format(tc, find()))


