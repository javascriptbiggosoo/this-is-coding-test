n = input()
덩어리 = n.split("-")

첫덩어리 = list(map(int, 덩어리[0].split("+")))
뒷덩어리 = []
for i in range(1, len(덩어리)):
    뒷덩어리.append(sum(list(map(int, 덩어리[i].split("+")))))

print(sum(첫덩어리) - sum(뒷덩어리))
