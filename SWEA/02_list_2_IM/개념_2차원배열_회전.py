import sys
import pprint

sys.stdin = open("개념_2차원배열_회전.txt", "r")
'''
5
12345
12345
12345
12345
12345
'''
# 중앙에서 오른쪽 끝부분 까지의 범위를 시계방향으로 한 번, 반시계방향으로 한 번 돌려보자
# 이건 수업 때 한 건 아니고 그냥 내가 만져보는거
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

# 시계방향으로 돌려보겠습니다.
mid = N//2
temp = []   # 범위 내의 숫자들
for i in range(mid, N):
    for j in range(mid, N):
        temp.append(arr[i][j])

for i in range(mid, N):
    for j in range(mid, N):
        arr[j][i] = temp.pop(0)
# pprint.pprint(arr)

###
# 반시계방향으로 돌려보겠습니다.(원상 복귀)
temp = []   # 범위 내의 숫자들
for i in range(mid, N):
    for j in range(mid, N):
        temp.append(arr[i][j])
for i in range(mid, N):
    for j in range(mid, N):
        arr[N-1+mid-j][i] = temp.pop(0)
# pprint.pprint(arr)

###
# 함수로
# (1, 1) (3, 4) 돌려보자
def rotate(a, b, c, d):
    temp = []
    for r in range(a, c+1):
        for c in range(b, d+1):
            temp.append(arr[r][c])
    for r in range(a, c+1):
        for c in range(b, d+1):
            arr[c][r] = temp.pop(0)
    return pprint.pprint(arr)


# rotate(1, 1, 3, 3)

###
# 여러번 돌리기

v1, v2, v3, v4 = 1, 1, 3, 3
for i in range(4):
    if i % 4 == 0:
        continue
    if i % 4 == 1:
        rotate(v1, v2, v3, v4)
    if i % 4 == 2:
        rotate(v1, v2, v3, v4)
        rotate(v1, v2, v3, v4)
    if i % 4 == 3:
        rotate(v1, v2, v3, v4)
        rotate(v1, v2, v3, v4)
        rotate(v1, v2, v3, v4)
