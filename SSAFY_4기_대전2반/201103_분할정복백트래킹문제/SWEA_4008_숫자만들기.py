# def calc():
#     ans = nums[0]
#     for i in range(1, N):
#         if op[i-1]== '+':
#             ans = ans + nums[i]
#         elif op[i-1]=='-':
#             ans = ans -nums[i]
#         elif op[i-1] == '*':
#             ans = ans * nums[i]
#         else:
#             ans = int(ans/ nums[i])
#     return ans
#
#
# def permutation(idx):
#     global minV, maxV
#     if idx == N - 1:
#         tmp = calc()
#
#         minV = min(minV, tmp)
#         maxV = max(maxV, tmp)
#         return
#
#     for i in range(idx, N - 1):
#         op[i], op[idx] = op[idx], op[i]
#         permutation(idx + 1)
#         op[i], op[idx] = op[idx], op[i]
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     op_cnt = list(map(int, input().split()))
#     nums = list(map(int, input().split()))
#
#     op = []
#     op += list('+' for _ in range(op_cnt[0]))
#     op += list('-' for _ in range(op_cnt[1]))
#     op += list('*' for _ in range(op_cnt[2]))
#     op += list('/' for _ in range(op_cnt[3]))
#
#     minV = 987654321
#     maxV = -987654321
#
#     permutation(0)
#
#     print("#{} {}".format(tc, maxV-minV))

###################위에는 시간터짐 ㅠ
op_dict = {0: '+', 1: '-', 2: '*', 3: '/'}


def calc(op):
    ans = nums[0]
    for i in range(1, N):
        if op[i - 1] == '+':
            ans = ans + nums[i]
        elif op[i - 1] == '-':
            ans = ans - nums[i]
        elif op[i - 1] == '*':
            ans = ans * nums[i]
        else:
            ans = int(ans / nums[i])
    return ans


def permutation(idx, o):
    global minV, maxV
    if idx == N - 1:
        tmp = calc(o)

        minV = min(minV, tmp)
        maxV = max(maxV, tmp)
        # print(o)
        return

    for i in range(len(op_cnt)):
        if op_cnt[i]:
            o[idx] = op_dict[i]
            op_cnt[i] -= 1
            permutation(idx + 1, o)
            op_cnt[i] += 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    op_cnt = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    minV = 987654321
    maxV = -987654321

    permutation(0, [0] * (N - 1))

    print("#{} {}".format(tc, maxV - minV))
