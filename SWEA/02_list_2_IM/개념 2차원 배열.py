# 2차원배열
# 1차원 리스트를 묶어놓은 리스트
# 
# 2차원 배열 선언
arr = [[0,1,2,3],[4,5,6,7]]
print(arr)

arr_1 = [0] * 5
# print(arr_1)
arr = [[0] * 5  for _ in range(5)]
for row in arr:
    print(row)

# 2차원 배열 입력받기
'''
3 4
0 1 0 0
0 0 0 0
0 0 1 0
'''
N,M = map(int,input().split())
mylist = [0 for i in range(N)]  #1차원 배열초기화

for i in range(N):
    mylist[i] = list(map(int,input().split()))  #1차원 배열 입력받아서 -> 리스트(1차원)로
print(mylist)

# 혹은

mylist = [list(map(int, input().split())) for _ in range(N)]
print(mylist)













