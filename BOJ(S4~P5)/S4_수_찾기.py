# 3트,, 괄호!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 아!!!!!!!
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
targets = list(map(int, input().split()))


def bs(arr, target, st, ed):
    if st > ed:
        return 0
    mid = (ed + st) // 2  # ------------------여기 괄호 안했음 하....ㅋㅋㅋㅋㅋ
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return bs(arr, target, st, mid - 1)
    else:
        return bs(arr, target, mid + 1, ed)


for target in targets:
    print(bs(arr, target, 0, n - 1))


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
