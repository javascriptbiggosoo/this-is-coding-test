# https://www.acmicpc.net/problem/10828
# 1트, 시간초과.. 이게 시간초과라니 지금은 감이 안잡힌다..
n = int(input())

stack = []


def stack_machine(o):
    if o[:2] == "pu":
        push = int(o[5:])
        stack.append(push)
    elif o == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    elif o == "size":
        print(len(stack))
    elif o == "empty":
        if len(stack):
            print(0)
        else:
            print(1)
    elif o == "top":
        try:
            print(stack[-1])
        except:
            print(-1)


for i in range(n):
    order = input()
    stack_machine(order)
