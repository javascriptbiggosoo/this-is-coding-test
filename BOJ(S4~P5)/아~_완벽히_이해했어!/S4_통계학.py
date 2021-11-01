import sys

n = int(input())
arr = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])


산평 = round(sum(arr) / n)
print(산평)

중값 = arr[n // 2]
print(중값)

빈도 = 1
빈값 = arr[0]
빈값들 = [arr[0]]
cnt = 1
for i in range(1, n):
    # 같은 숫자면 카운트를 증가시키고 아니라면 카운트를 초기화한다.
    if arr[i] == arr[i - 1]:
        cnt += 1
    else:
        cnt = 1
    # 카운트가 기존 최빈값을 넘었을 경우
    if cnt > 빈도:
        빈도 = cnt
        빈값 = arr[i]
        빈값들 = []
        빈값들.append(빈값)
    elif cnt == 빈도:
        빈값 = arr[i]
        빈값들.append(빈값)
# print(빈값들)
if len(빈값들) > 1:
    print(sorted(빈값들)[1])
else:
    빈값 = 빈값들[0]
    print(빈값)

범위 = arr[-1] - arr[0]
print(범위)
