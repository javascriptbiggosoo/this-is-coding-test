# 1트 성공, dp는 메모이제이션만 알면 별거없구나
T = int(input())


arr = [0] * 101
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2

for i in range(5, 101):
    arr[i] = arr[i - 1] + arr[i - 5]

for tc in range(T):
    print(arr[int(input())])
