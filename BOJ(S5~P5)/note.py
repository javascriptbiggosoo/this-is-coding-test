# 1트, 그런데 이제 준내 오래걸린..
세로, 가로 = map(int, input().split())
arr = [[] for _ in range(세로)]

for i in range(세로):
    줄 = input()
    for j in range(가로):
        arr[i].append(줄[j])

n = 0
for i in range(세로):
    if 가로 % 2 - 1:
        n += 1
    for j in range(가로):
        n += 1
        if n % 2:
            if arr[i][j] == "W":
                arr[i][j] = 0
            else:
                arr[i][j] = 1
        else:
            if arr[i][j] == "B":
                arr[i][j] = 0
            else:
                arr[i][j] = 1

res = []
for i in range(세로 - 8 + 1):
    for j in range(가로 - 8 + 1):
        합 = 0
        for ii in range(i, i + 8):
            for jj in range(j, j + 8):
                합 += arr[ii][jj]
        res.append(min(합, abs(합 - 64)))

print(min(res))
