import sys
sys.stdin = open('4366.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    two = input()
    three = input()
    two_list = []
    for i in range(len(two)):
        two_list.append(int(two[len(two)-1-i])*(2**i))
    # print(two_list)
    three_list = []
    for i in range(len(three)):
        three_list.append(int(three[len(three)-1-i])*(3**i))
    # print(three_list)
    adj_two = []
    for i in range(len(two_list)):
        if two_list[i]:     # 0아니면
            adj_two.append(sum(two_list)-two_list[i])
        else:               # 0이면
            adj_two.append(sum(two_list)+2**i)
    # print(adj_two)
    bit_three = []
    cnt = 0
    for i in three_list:
        bit_three.append(i // 3**cnt)
        cnt += 1
    # print(bit_three)
    adj_three = []
    for i in range(len(three_list)):
        if bit_three[i] == 0:
            adj_three.append(sum(three_list)+3**i)
            adj_three.append(sum(three_list)+(3**i)*2)
        elif bit_three[i] == 1:
            adj_three.append(sum(three_list)-three_list[i])
            adj_three.append(sum(three_list)+3**i)
        else:
            adj_three.append(sum(three_list)-three_list[i])
            adj_three.append(sum(three_list)-3**i)
    # print(adj_three)
    for i in adj_three:
        if i in adj_two:
            ans = i
    print(f'#{tc} {ans}')

# # T's

# def check(num, notation):
#     change_num = int(num, notation)

#     idx = len(num)-1
#     for i in map(int, num):
#         for j in range(notation):
#             if i == j:
#                 continue

#             tmp = change_num - i * (notation ** idx) + j * (notation ** idx)
#             if tmp not in ans:
#                 ans.append(tmp)
#             else:
#                 return tmp

#         idx -= 1


# for tc in range(1, int(input())+1):
#     num2 = input()
#     num3 = input()

#     # 한비트씩 바꾼 10진수를 저장할 리스트
#     ans = []

#     check(num2, 2)
#     print("#{} {}".format(tc, check(num3, 3)))
