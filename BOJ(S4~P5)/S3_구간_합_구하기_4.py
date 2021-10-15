# 2트, 1트에선 횟수마다 sum()연산을 하면서 시간이 엄청 걸렸는데 누적합을 미리 만들어두고 그것들을 이용하면 훨씬 자원이 절약된다
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

누적합 = [0]
for i in range(n):
    누적합.append(누적합[-1] + arr[i])

# print(누적합)
for tc in range(m):
    st, ed = map(int, sys.stdin.readline().rstrip().split())
    print(누적합[ed] - 누적합[st - 1])


# 1트, 시간초과
# import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))

# for tc in range(m):
#     st, ed = map(int, sys.stdin.readline().rstrip().split())
#     print(sum(arr[st - 1 : ed]))
