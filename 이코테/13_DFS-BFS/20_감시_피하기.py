# https://www.acmicpc.net/problem/18428
n = int(input())
classroom = [list(input().split()) for _ in range(n)]
print(classroom)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


# T 맵핵 켜기
def 맵핵():
    return


def 설치(num):
    r = num // n
    c = num % n
    return [r, c]


# 방해물 3개 설치
for i in range(0, n - 1):
    좌표 = 설치(i)
    classroom[좌표[0]][좌표[1]] = "O"
    for j in range(i + 1, n):
        좌표 = 설치(j)
        classroom[좌표[0]][좌표[1]] = "O"
        for k in range(j + 1, n + 1):
            좌표 = 설치(j)
            classroom[좌표[0]][좌표[1]] = "O"
