import sys

sys.stdin = open("input.txt", "r")

# 숫자카드
# 리스트 받는 애들중에 제일 많은 친구
# 최대수가 같다면 더 큰 친구

T = int(input())    # 3흡수기

for tc in range(1, T + 1):
    N = int(input())    # 길이 흡수기
    M = input()
    arr = []            # 받은거 리스트로 바꿔줌
    for m in M:
        arr.append(int(m))
        arr.sort()          # 그걸 정렬
        cnts = [0] * (max(arr) + 1)
        for i in arr:
            cnts[i] += 1
        most = max(cnts)     # 제일 많은거 갯수야
        counter = 0
        result = 0
        for j in cnts:
            if j == most:
                result = counter
            counter += 1

    print('#{} {} {}'.format(tc, result, most))


# 내 코드는 아님! 근데 개쩐다..
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())  # 쓰이는건 아닌데 그냥 입력 흡수기
#     num_list = list(map(int, input()))
#
#     max_num = -1
#     max_cnt = 0
#     for i in range(10):
#         if num_list.count(i) >= max_cnt:
#             max_cnt = num_list.count(i)
#             max_num = i
#
#     print(f'#{test_case} {max_num} {max_cnt}')