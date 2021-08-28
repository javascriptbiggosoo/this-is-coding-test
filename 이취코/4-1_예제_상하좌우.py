N = int(input())
plan = list(input().split())
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
controller = {"L": 0, "R": 1, "U": 2, "D": 3}

nr = 1
nc = 1
for i in range(len(plan)):
    if (
        len(plan) >= nr + dr[controller[plan[i]]] > 0
        and len(plan) >= nc + dc[controller[plan[i]]] > 0
    ):
        nr = nr + dr[controller[plan[i]]]
        nc = nc + dc[controller[plan[i]]]

print(nr, nc)

# N = int(input())
# x, y = 1, 1
# plans = input().split()

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# directions = ["U", "D", "L", "R"]

# for plan in plans:
#     for i in range(len(directions)):
#         if plan == directions[i]:
#             nx += x + dx[i]
#             ny += y + dy[i]
#     if nx < 1 or ny < 1 or nx > N or ny > N:
#         continue
#     x, y = nx, ny
#     print(x, y)
