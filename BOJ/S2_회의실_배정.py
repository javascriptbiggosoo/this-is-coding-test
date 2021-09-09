# 1트 시간초과
# 정렬후에 for문을 한 번만 돌려야 할듯.
# lambda 사용법도 알아놔야 할듯.
n = int(input())
result = 0
모든회의 = [list(map(int, input().split())) for _ in range(n)]
while True:
    마침 = 2 ** 31
    for 회의 in 모든회의:
        if 마침 >= 회의[1]:
            마침 = 회의[1]
    # print(마침)
    모든회의 = [회의 for 회의 in 모든회의 if 회의[0] >= 마침]
    # print(모든회의)
    if 마침 == 2 ** 31:
        break
    result += 1
print(result)


# 2트
