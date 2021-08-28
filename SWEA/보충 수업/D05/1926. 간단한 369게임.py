# while로만 풀어보자

import sys

sys.stdin = open("1926.txt", "r")

T = int(input())
i = 0
while T - i > 0:
    i += 1

    if i >= 10:
        mok = i // 10   # 1 2 3 4 5
    else:
        mok = 1

    if ((i % 10) % 3 == 0) and i % 10 != 0 and (mok % 3 == 0):
        print('--', end=' ')

    elif (i % 10) % 3 == 0 and i % 10 != 0:
        print('-', end=' ')
    elif mok % 3 == 0:
        print('-', end=' ')
    else:
        print(i, end=' ')

# 엄혜주 선생님의 코드
# N = int(input())
# for i in range(1,N+1):
#     # print(i, end=' ')
#     n = i   #숫자 저장
#     is369 = False #369인지 아닌지 판별하기 위한 변수 : flag
#     while n > 0 :   #숫자가 0보다 큰 동안 반복
#         d = n % 10  #1의자리 숫자 가져오기
#         n = n // 10 #n을 갱신 (1의자리 수 버리기)
#         if d == 3 or d == 6 or d == 9:
#             print("-",end="")
#             is369 = True
#     #반복 종료 후 369가 아니면?
#     if not is369:
#         print(i, end=" ")
#     else:   #369였으면 공백만 추가
#         print(" ",end="")