# row col square 각각을 체크하고 세가지가 모두 트루 뱉을 때 작동하는 방식도 만들 수 있을 듯 한데(구현은 더 쉬울 것 같은데) 시간이 없어서 다음에 해보자   라고 썼는데 성장하고 보니까 굳이 안나눠도 되는구나라는걸 알게됨 ㅋㅋ

import sys

sys.stdin = open("1974.txt", "r")


def check():        # (2) 스도쿠 판 검사 clear
    for i in range(9):
        row = [0] * 10      # (3) 행, 열을 돌아서 숫자가 나오는 칸에 1로 바꿔줄 예정, (복기 할 때 이게 가장 어려웠는데 row 와 col을 한 방에 해서 헷갈리기 쉬웠다. 최하단 반복문 위에서 실행해준다는거, 초심자는 row cal square 따로 하는게 ㄹㅇ 맞을듯)
        col = [0] * 10
        for j in range(9):          # (4) 2차원 배열 한칸씩 따져봅니다.
            if row[pann[i][j]]:     # (5) 중복이 발견됐다? 어림도 없지 바로 0 return ㅋㅋㅋ
                return 0
            if col[pann[j][i]]:
                return 0
            row[pann[i][j]] = 1     # (6) 확인한 친구는 1로 만들어줘요
            col[pann[j][i]] = 1

            if i % 3 == 0 and j % 3 == 0:   # (7) 3x3검사
                square = [0] * 10
                for k in range(3):
                    for l in range(3):
                        if square[pann[i+k][j+l]]:
                            return 0
                        square[pann[i+k][j+l]] = 1
    return 1


T = int(input())        # (1) 스도쿠 판 만들기
for tc in range(1, 1 + T):
    pann = [list(map(int, input().split())) for _ in range(9)]

    if check():
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))


'''
혼자 풀었다!!!! 미묘하게 다름!! 시험 대비라서 정리 안했는데 나중에 하나로 통합하자

T = int(input())

def check(sudoku):

    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            if row[sudoku[i][j]] == 0:
                row[sudoku[i][j]] = 1
            else:
                return 0
            if col[sudoku[j][i]] == 0:
                col[sudoku[j][i]] = 1
            else:
                return 0

    for i in range(9):
        for j in range(9):
            if (i % 3) == 0 and (j % 3) ==0:
                square = [0] * 10
                for r in range(3):
                    for c in range(3):
                        if square[sudoku[i+r][j+c]] == 0:
                            square[sudoku[i+r][j+c]] = 1
                        else:
                            return 0
    return 1


for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = check(arr)
    print('#{} {}'.format(tc, ans))

'''
