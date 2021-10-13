# 2트.. 입력을 이쁘게 받아보자

import sys

n = int(input())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]

# print(arr)
s = []

for i in arr:
    if i[:2] == "pu":
        s.append(i[5:])
    elif i == "pop":
        if len(s):
            print(s.pop())
        else:
            print(-1)
    elif i == "size":
        print(len(s))
    elif i == "empty":
        if len(s):
            print(0)
        else:
            print(1)
    else:
        if len(s):
            print(s[-1])
        else:
            print(-1)


# https://www.acmicpc.net/problem/10828
# 1트, 시간초과.. 이게 시간초과라니 지금은 감이 안잡힌다..
# n = int(input())

# stack = []


# def stack_machine(o):
#     if o[:2] == "pu":
#         push = int(o[5:])
#         stack.append(push)
#     elif o == "pop":
#         try:
#             print(stack.pop())
#         except:
#             print(-1)
#     elif o == "size":
#         print(len(stack))
#     elif o == "empty":
#         if len(stack):
#             print(0)
#         else:
#             print(1)
#     elif o == "top":
#         try:
#             print(stack[-1])
#         except:
#             print(-1)


# for i in range(n):
#     order = input()
#     stack_machine(order)
