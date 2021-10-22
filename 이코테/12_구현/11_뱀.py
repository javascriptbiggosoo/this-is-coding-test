# https://www.acmicpc.net/problem/3190
import sys
from collections import deque
import pprint

n = int(sys.stdin.readline().rstrip())
판 = [[0] * (n + 1) for _ in range(n + 1)]
# 사과 수
k = int(sys.stdin.readline().rstrip())
for i in range(k):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    판[r][c] = 9
pprint.pprint(판)
# 방향 전환
l = int(sys.stdin.readline().rstrip())
# 에너미 컨트롤러
EC = []
for i in range(l):
    t, c = sys.stdin.readline().rstrip().split()
    EC.append([int(t), c])

뱀 = deque([[1, 1]])  
dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

# 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
while 뱀:
