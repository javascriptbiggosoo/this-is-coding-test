# 단축키.. "글자 글자." 적고 엔터 누르니까 이프문이 생겨버리네...... 옵션 고를 수 있네.. while 이런 것도.. 쓸모없나
import sys


sys.stdin = open("input.txt", "r")

T = int(input())

def prc(row, col):
    mini = 0
    for i in range(M):
        for j in range(M):
            mini += arr[row+i][col+j]
    return mini

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            ans.append(prc(r, c))
    print(max(ans))
