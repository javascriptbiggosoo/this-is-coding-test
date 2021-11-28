#  1트 성공, 닫는 괄호는 가장 늦게 여는 괄호와 짝이다. 닫는 괄호가 올때마다 pop을 해주면 된다. 여는 괄호가 없을때 닫는괄호부터 온다면 틀린거다
T = int(input())

for tc in range(T):
    vps = input()
    arr = []
    for i in vps:
        if i == "(":
            arr.append("(")
        else:
            if len(arr):
                arr.pop()
            else:
                arr.append("false")
                break
    if len(arr):
        print("NO")
    else:
        print("YES")
