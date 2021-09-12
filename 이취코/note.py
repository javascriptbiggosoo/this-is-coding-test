n = int(input())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
에너미컨트롤러 = ["U", "D", "L", "R"]

plans = input().split()
x = 1
y = 1
for plan in plans:
    for i in range(len(에너미컨트롤러)):
        if plan == 에너미컨트롤러[i]:
            nx = dx[i]
            ny = dy[i]
            if x + nx > 0 and x + nx <= n and y + ny > 0 and y + ny <= n:
                x += nx
                y += ny


print(x, y)
