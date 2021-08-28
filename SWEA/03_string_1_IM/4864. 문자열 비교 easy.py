import sys

sys.stdin = open("../list_2/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()  # 짧은거
    str2 = input()  # 긴거
    result = 0
    for i in range(len(str2) - len(str1)+1):
        cnt = 0     # 이거만 발상하면 나머지는 너무 쉬움 지금
        for j in range(len(str1)):
            if str2[i+j] == str1[j]:
                cnt += 1
            else:
                break
        if cnt == len(str1):
            result = 1
    print('#{} {}'.format(test_case, result))






