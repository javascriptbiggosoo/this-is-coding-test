#2차원배열
#1차원 리스트를 묶어놓은 리스트

#2차원 배열 선언
# arr = [[0,1,2,3],[4,5,6,7]]
# print(arr)

# arr_1 = [0] * 5
# # print(arr_1)
# arr = [[0] * 5  for _ in range(5)]
# for row in arr:
#     print(row)

#2차원 배열 입력받기
'''
3 4
0 1 0 0
0 0 0 0
0 0 1 0
'''
#방법1
# N,M = map(int,input().split())
# mylist = [0 for i in range(N)]  #1차원 배열초기화
# # print(mylist)
# # mylist[0] = list(map(int,input().split()))  #1차원 배열 입력받아서 -> 리스트(1차원)로
# # mylist[1] = list(map(int,input().split()))  #1차원 배열 입력받아서 -> 리스트(1차원)로
# # mylist[2] = list(map(int,input().split()))  #1차원 배열 입력받아서 -> 리스트(1차원)로
#
# for i in range(N):
#     mylist[i] = list(map(int,input().split()))  #1차원 배열 입력받아서 -> 리스트(1차원)로

# for row in mylist:
#     print(row)

#방법2
# N,M = map(int,input().split())
# mylist =[]
#
# for i in range(N):
#     #한줄읽어서 빈칸으로 나누고 인트로 형변환 그리고 리스트로 변환
#     #mylist에 추가 (append)
#     mylist.append(list(map(int,input().split())))


#방법3
# N,M = map(int,input().split())
# mylist = [list(map(int,input().split())) for _ in range(N)]
# #이걸 N번 반복하면서 mylist에 넣기
#
# for row in mylist:
#     print(row)

# 2차원 배열 순회
# 행우선 순회
# 열우선 순회
# 지그재그 순회
# 델타
arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

# 행우선 순회
# for j in range(len(arr[0])):
#     print(arr[0][j], end= " ")
# print()
# for j in range(len(arr[1])):
#     print(arr[1][j], end= " ")
# print()
# for j in range(len(arr[2])):
#     print(arr[2][j], end= " ")
# print()
# for j in range(len(arr[3])):
#     print(arr[3][j], end= " ")

# for i in range(len(arr)):
#     for j in range(len(arr[3])):
#         print(arr[i][j], end= " ")
#     print()

#열우선순회
# arr = [[1,2,3,4],
#        [5,6,7,8],
#        [9,10,11,12],
#        [13,14,15,16]]
#
# for i in range(len(arr)):
#     for j in range(len(arr[3])):
#         print(arr[j][i], end= " ")  #j : 안쪽 for문, i : 바깥쪽 for문
#     print()

# arr = [[1,2,3,4],
#        [5,6,7,8],
#        [9,10,11,12],
#        [13,14,15,16]]
# #지그재그
# for i in range(len(arr)):
#     if i % 2 == 0:
#         #짝수행일때
#         for j in range(len(arr[i])):
#             print(arr[i][j], end= " ")
#     else:
#         #홀수행일때
#         for j in range(len(arr[i])-1,-1,-1):
#             print(arr[i][j], end= " ")
#     print()

arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10,11,12],
       [13,14,15,16]]
dr = [-1,0,1,0]
dc = [0,1,0,-1]

for r in range(len(arr)):
    for c in range(len(arr[r])):
        # r,c = 1,1   #사실은...전 좌표에서 확인하고 싶음!
        #다음위치 계산
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr <0 or nr >=len(arr) or  nc < 0 or nc >= len(arr): continue
            print(nr,nc,arr[nr][nc], end= "/")
        print()

# #상
# nr = r + dr[0]
# nc = c + dc[0]
# print(nr,nc,arr[nr][nc])
# #우
# nr = r + dr[1]
# nc = c + dc[1]
# print(nr,nc,arr[nr][nc])
# #하
# nr = r + dr[2]
# nc = c + dc[2]
# print(nr,nc,arr[nr][nc])
# #좌
# nr = r + dr[3]
# nc = c + dc[3]
# print(nr,nc,arr[nr][nc])





















