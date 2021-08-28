import sys
sys.stdin = open('1206.txt', 'r')

# tc가 10개래
for tc in range(1, 11):
    len_BDs = int(input())
    BD = list(map(int, input().split()))
    res = 0     # 조망권 있는 것 갯수
    for i in range(len_BDs):
        left_max = 0
        right_max = 0
        for left in range(1, 3):    # 1, 2
            if i - left >= 0:
                if BD[i - left] > left_max:
                    left_max = BD[i-left]
        for right in range(1, 3):   # 1, 2
            if i + right < len_BDs:
                if BD[i + right] > right_max:
                    right_max = BD[i+right]         # 나중에 위엣 것과 합쳐보자
        both_max = max([left_max, right_max])
        if (BD[i] - both_max) > 0:    # 기준 건물의 조망권이 1칸 이상일 경우
            res += BD[i] - both_max

    print('#{} {}'.format(tc, res))

'''
하영이 풀이
for tc in range(1, 11):
    N = int(input())
    bd = list(map(int, input().split()))
    res = 0
    for i in range(2, N - 2):
        b = [bd[i - 2], bd[i - 1], bd[i + 1], bd[i + 2]]
        idx = max(b)
        if bd[i] > idx:
            res += bd[i] - idx
    print('#{} {}'.format(tc, res))
'''
