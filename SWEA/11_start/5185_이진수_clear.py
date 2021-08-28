# 개선해야겠지요

import sys
sys.stdin = open('5185.txt', 'r')

sixteen_2_2 = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

T = int(input())
for tc in range(1, 1 + T):
    len_s, s = map(str, input().split())
    print('#'+str(tc), end=' ')
    for i in s:
        print(sixteen_2_2[i], end='')
    print()

###
# 2. int 내장 함수 이용
for tc in range(1, int(input()) + 1):
    N, HEX = input().split()
    HEX = int(HEX, 16)
    HEX = format(HEX, 'b')
    if len(HEX) != int(N) * 4:
        HEX = '0' * (int(N) * 4 - len(HEX)) + HEX
    print("#{} {}".format(tc, HEX))
