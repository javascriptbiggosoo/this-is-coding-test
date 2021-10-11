# 1트, 메모리 초과
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(n):
    print(arr[i])
