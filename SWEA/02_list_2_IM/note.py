import sys

sys.stdin = open("1974.txt", "r")

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
