# https://www.acmicpc.net/problem/1676
n = int(input())

# N!을 구함
fact = 1
for i in range(1, n + 1):
    fact *= i

# N!에서 0탐색
target = str(fact)
cnt = 0
for i in range(len(target)):
    # print(cnt)
    if target[-(i + 1)] == "0":
        cnt += 1
    else:
        break

print(cnt)
