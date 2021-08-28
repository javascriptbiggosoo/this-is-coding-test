import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    diff = max(numbers) - min(numbers)
    print(f'#{tc} {diff}')


# 내장 함수 안쓰기
# def get_max(init_num):
#     my_max = init_num[0]
#     for i in range(1, len(init_num)):
#         if my_max < init_num[i]:
#             my_max = init_num[i]
#
#     return my_max
#
# def get_min(init_num):
#     my_min = init_num[0]
#     for i in range(1,len(init_num)):
#         if my_min > init_num[i]:
#             my_min = init_num[i]
#
#     return my_min
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     init_num = list(map(int, input().split()))
#     result = get_max(init_num) - get_min(init_num)
#     print(f'#{tc} {result}')