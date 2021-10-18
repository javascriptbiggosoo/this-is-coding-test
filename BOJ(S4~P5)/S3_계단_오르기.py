# 1트 성공. 마지막 도착 계단은 반드시 밟아야 한다. 부분을 놓치고 d[i-1]도 비교대상에 넣었었다. 그걸 빼고나니 제대로 돌아감
import sys

n = int(sys.stdin.readline().rstrip())
arr = [0]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
d = [0] * (n + 1)
d[0] = 0
d[1] = arr[1]
if n > 1:
    d[2] = arr[1] + arr[2]
    if n > 2:
        # 한칸 점프는 못할 수도 있지만
        # 두칸 점프는 무조건 할 수 있다
        # 마지막 도착 계단은 반드시 밟아야 한다.
        for i in range(3, n + 1):
            # 두칸 뒤에서 두칸 점프
            d[i] = d[i - 2] + arr[i]
            # 세칸 뒤에서 두칸 점프 후 1점프
            d[i] = max(d[i], d[i - 3] + arr[i - 1] + arr[i])
# print(arr)
# print(d)

print(d[n])
