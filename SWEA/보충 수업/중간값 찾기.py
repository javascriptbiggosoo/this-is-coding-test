import sys
sys.stdin = open('input_2063.txt','r')
N = int(input())
# 한 줄 읽어서 공백문자로 구분하고 그걸 정수형 리스트로 만들어서 변수에 저장
arr = list(map(int,input().split()))
# print(arr)
for i in range(0, N-1):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j], arr[i]
    print(arr)
# print(arr[N//2])


