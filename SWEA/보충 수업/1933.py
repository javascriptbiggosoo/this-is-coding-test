'''
10
'''
# 약수 : 어떤수 N을 나눠서 떨어지는 수
N = int(input())
for i in range(1, N+1):     # range(시작,끝) range(1,10) : [1,2,3...9] => 10은 포함안함
    # print(i)
    if N % i == 0:  # i는 약수임
        print(i,end=' ')
print()
