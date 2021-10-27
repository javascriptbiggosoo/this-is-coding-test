# 1트, 손도 못댔으니 손댔으면 당연 틀림, 일단 완전탐색해도 된다는 판단 자체를 못했고
# 최적의 풀이를 계속 고민했는데, 완전탐색이면 충분한 문제였다.
# 그리고 알고 난 이후에도 조합을 구현하는데 있어 어려움이 느껴졌음.

# https://www.acmicpc.net/problem/14502
import pprint

세로, 가로 = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(세로)]
pprint.pprint(arr)

# 벽 세우기 완전탐색(조합..)

# 완전탐색 순간마다 dfs돌리기

# 그 중 안전영역 제일 큰 값을 저장해두기
