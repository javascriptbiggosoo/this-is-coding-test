import sys

sys.stdin = open("1954.txt", "r")


dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    r = 0
    c = 0
    num = 1     # 칸 진행 횟수
    turn = 0

    while num <= N * N:
        arr[r][c] = num
        num += 1

        nr = r + dr[turn]
        nc = c + dc[turn]

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:    # 마지막 == 0 안해주면 한바퀴만 뒤지게 돈다
            r = nr
            c = nc
        else:
            turn = (turn + 1) % 4
            r += dr[turn]
            c += dc[turn]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


# # T's
# import sys

# sys.stdin = open("1954.txt", "r")

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     nums = [[0]*N for _ in range(N)]

#     K = N # 이동거리
#     d = 1 # 방향
#     row = 0 # 행
#     col = -1 # 열 (초기에는 수평이동이므로 -1)
#     num = 1 # 넣을 값

#     while True:
#         # 수평이동
#         for c in range(K):
#             col += d
#             nums[row][col] = num
#             num += 1
#         # 수평이동 끝 이제 수직이동
#         K -= 1
#         if K == 0:
#             break
#         # 수직이동
#         for r in range(K):
#             row += d
#             nums[row][col] = num
#             num += 1
#         # 수직이동이 끝 수평이동
#         d *= -1

#     print("#{}".format(tc))
#     for i in range(N):
#         for j in range(N):
#             print(nums[i][j], end=" ")
#         print()

