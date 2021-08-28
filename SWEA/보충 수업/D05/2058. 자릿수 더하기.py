# while로만 풀어보자

import sys

sys.stdin = open("2058.txt", "r")

T = input()
arr = []
cnt = -1
while cnt+2 <= len(T):
    cnt += 1
    mok = int(T) // (10**cnt)
    number = mok % 10     # 6789 % 10 = 9
    arr.append(number)

print(sum(arr))

# 엄혜주 선생님의 코드
# 자릿수더하기
# '''
# 6789
# '''
# N = int(input())
# # print(N)
# sum = 0
# #N을 갱신 -> N이 0이 되면 그만해 -> 0이 아닌동안 돌아
# while N != 0:
#     d = N % 10
#     sum += d
#     N = N // 10
# print(sum)
