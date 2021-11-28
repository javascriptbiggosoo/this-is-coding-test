# 1트 성공, 밑에서부터 최대값 하나씩 확인해봄

# https://www.acmicpc.net/problem/1932
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

curr = arr[n - 1]
while n > 0:
    for i in range(n - 1):
        curr[i] = max(arr[n - 2][i] + curr[i], arr[n - 2][i] + curr[i + 1])
    n -= 1
    # print(curr)

print(curr[0])
