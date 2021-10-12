# 오잉? 맞왜맞.. 이거 왜 맞냐고~~~ 아래거랑 차이 없는거아님?
from sys import stdin, stdout

n = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())


def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m - 1)
    else:
        return binary(l, N, m + 1, end)


for l in M:
    start = 0
    end = len(N) - 1
    print(binary(l, N, start, end))


# 2트, 반복문은 시간초과.. 재귀는 런타임 에러.. 어떡하지?
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()


# m = int(input())
# targets = list(map(int, input().split()))


# for i in range(m):
#     target = targets[i]
#     ans = 0
#     st = 0
#     ed = n - 1
#     while st <= ed:
#         mid = ed + st // 2
#         if arr[mid] == target:
#             ans = 1
#             break
#         elif arr[mid] > target:
#             ed = mid - 1
#         else:
#             st = mid + 1
#     print(ans)


# 1트, 런타임 에러
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()

# m = int(input())
# targets = list(map(int, input().split()))


# def bs(arr, target, st, ed):
#     if st > ed:
#         return 0
#     mid = ed + st // 2
#     if arr[mid] == target:
#         return 1
#     elif arr[mid] > target:
#         return bs(arr, target, st, mid - 1)
#     else:
#         return bs(arr, target, mid + 1, ed)


# for target in targets:
#     print(bs(arr, target, 0, n - 1))
