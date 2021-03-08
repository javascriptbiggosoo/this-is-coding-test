N = int(input())
plan = list(input().split())
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
controller = {"L": 0, "R": 1, "U": 2, "D": 3}

nr = 1
nc = 1
for i in range(len(plan)):
    if len(plan) >= nr+dr[controller[plan[i]]] > 0 and len(plan) >= nc+dc[controller[plan[i]]] > 0:
        nr = nr+dr[controller[plan[i]]]
        nc = nc+dc[controller[plan[i]]]

print(nr, nc)
