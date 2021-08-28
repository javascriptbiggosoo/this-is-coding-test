# 스스로 풀었는데 꽤나 만족스럽습니당~~

import sys
sys.stdin = open('5186.txt', 'r')
#
# fn = 0.5
# two_list = []
# for i in range(12):
#     if i == 0:
#         two_list.append(fn)
#         continue
#     two_list.append(fn/(2**i))   # 소수 이진수 열두개 만듬
#
# T = int(input())
# for tc in range(1, 1 + T):
#     target = float(input())
#     res = ''
#     for i in range(12):
#         if target >= two_list[i]:
#             res += "1"
#             target -= two_list[i]
#         else:
#             res += "0"
#         if target == 0:
#             break
#
#     if target:
#         print(f'#{tc} overflow')
#     else:
#         print(f'#{tc} {res}')

###
# 명균's 감동적인 풀이
for tc in range(1, int(input()) + 1):
    N = float(input())
    ans = ''

    while True:
        N *= 2
        ans += str(N)[0]
        if N >= 1:
            N -= 1
        if N == 0:
            break

        if len(ans) >= 13:
            ans = 'overflow'
            break
    print("#{} {}".format(tc, ans))
