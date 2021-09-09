T = input()

li = list(map(int, input().split()))
res = 0
for i in range(len(li)):
    target = li[i]

    if target == 1:
        continue
    elif target == 2:
        res += 1
        continue

    for j in range(2, target):
        if j == target - 1:
            res += 1
        if target % j == 0:
            break

print(res)
