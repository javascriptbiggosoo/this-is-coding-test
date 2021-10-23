# 2트, 오케이 마이너스 붙이면 역순이구나
# 1트, 구현 방법 자체를 모르겠다 sort 내장함수 다루는법을 익히자
# https://www.acmicpc.net/problem/10825
import sys

n = int(sys.stdin.readline().rstrip())
arr = [list(sys.stdin.readline().rstrip().split()) for _ in range(n)]

# print(arr)

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in arr:
    print(i[0])
