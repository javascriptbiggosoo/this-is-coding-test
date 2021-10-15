# 1트, 시간초과
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for tc in range(m):
    st, ed = map(int, sys.stdin.readline().rstrip().split())
    print(sum(arr[st - 1 : ed]))
