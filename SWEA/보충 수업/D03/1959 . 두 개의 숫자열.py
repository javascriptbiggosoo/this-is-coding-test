import sys
sys.stdin = open("1959.txt", "r")

T = int(input())

for tc in range(1, 1 + T):
    trash = input()     # 안쓸래!
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))
    if len(N) > len(M):     # 라고 하고보니 트래쉬에 들어갈 입력값 쓸 수 있겠네.. 나중에 보면 수정해보자
        long = N
        short = M
    else:
        long = M
        short = N

    lenL = len(long)
    lenS = len(short)
    maxx = []
    for i in range(lenL - lenS + 1):    # 5 - 3 + 1
        ssum = []
        for j in range(lenS):
            ssum.append(short[j] * long[i+j])
        maxx.append(sum(ssum))

    print('#{} {}'.format(tc, max(maxx)))

#####
# 엄혜주 선생님의 코드
# 구간합 문제와 비슷합니다.
# 실시간 코딩인데 시간이 급해서 날림코딩(최솟값을 0으로 한 부분이라던가..)
# def solve(arr1,arr2): # 첫번째 짧은 두번째 긴 , 함수의 정의
#     len1 = len(arr1)
#     len2 = len(arr2)
#     maxV = 0      # 최소값으로 초기화
#     '''
#     12345
#     123
#      123
#       123
#     비교 시작위치?
#     0,1,2 -> 바깥쪽 for문의 범위 -> 0 ~ (긴문자열 길이 - 짧은문자열 길이) => 5-3 => 2
#     '''
#     for i in range(0,len2- len1 +1):    #비교 시작점
#         sum = 0
#         for j in range(0,len1): #짧은 문자열 반복
#             num = arr1[j] * arr2[i+j]      # 짧은 ; 0,1,2...0,1,2.
#                                         # 긴 문자열 : 0,1,2...1,2,3...2,3,4
#                                         #            0+ (0,1,2),1+(0,1,2) , 2 +(0,1,2)
#             sum += num
#         # print(sum,end=" ")
#         if maxV < sum :
#             maxV = sum
#     return maxV
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     A = list(map(int,input().split()))
#     B = list(map(int,input().split()))
#     # print(A)
#     # print(B)
#     # 숫자열 길이를 비교해서
#     # 짧은 숫자열, 긴 숫자열 순으로 매개변수로 해서 함수에 넘김
#
#     result = 0
#
#     if len(A) < len(B):
#         result = solve(A, B) # 첫번째 : 짧은, 두번째 : 긴
#     else:
#         result = solve(B, A)
#     print("#{} {}".format(tc, result))