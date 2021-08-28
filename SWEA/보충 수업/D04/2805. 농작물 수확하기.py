import sys
sys.stdin = open("2805.txt", "r")
'''
1
5
14054
44250
02032
51204
52212

'''

T = int(input())
for tc in range(1,T+1):
    #입력
    N = int(input())
    arr = [ list(map(int,input())) for _ in range(N)]
    #한줄읽어서 리스트로 만들고(행) 그걸 리스트에 담기(N번반복)
    # for row in arr:
    #     print(row)
    #계산
    #마름모 꼴로 수확할 수 있음
    # N//2까지는 1,3,5,7...로 증가
    # 그이후 부터는 5,3,1..로 감소
    sum = 0
    for i in range(0,N):
        if i <= N//2 :  #칸수 증가
            for j in range(N//2-i, N//2+i +1):
                sum += arr[i][j]
        else:           #칸수 감소
            for j in range(i-N//2,N-(i-N//2)):
                sum += arr[i][j]
    #출력
    print("#{} {}".format(tc, sum))
