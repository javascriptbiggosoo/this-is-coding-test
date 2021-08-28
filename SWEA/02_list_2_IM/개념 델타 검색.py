# 델타검색
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
N = 3
M = 4

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(N):      # 012
    for y in range(M):      # 0123
        for i in range(4):      # 에너미 컨트롤러! 0123
            testX = x+dx[i]     # 0 + 0
            testY = y+dy[i]     # 0 + -1
            # 출력문
            # if 0 <= testX < N and 0 <= testY < M:
            #     print(arr[testX][testY], end=' ')

#############################################

nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

r = 0   # 좌표
c = 1

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

for i in range(4):
    nr = r + dr[i]  # 좌표 + dr
    nc = c + dc[i]
    if nr < 0 or nr >= 3 or nc < 0 or nc >= 3:
        continue
    print(nums[nr][nc])
    # 이렇게도 가능
    # if 0 <= nr <3 and 0 <= nc <3:
    #     print(nums[nr][nc])