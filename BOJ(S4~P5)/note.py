T = int(input())

for tc in range(T):
    n = int(input())
    영 = [0] * (n + 2)
    영[0] = 1
    영[1] = 0
    일 = [0] * (n + 2)
    일[0] = 0
    일[1] = 1
    for i in range(2, n + 1):
        영[i] = 영[i - 1] + 영[i - 2]
        일[i] = 일[i - 1] + 일[i - 2]
    print(영)
    print(일)
    print(영[-2], 일[-2])
