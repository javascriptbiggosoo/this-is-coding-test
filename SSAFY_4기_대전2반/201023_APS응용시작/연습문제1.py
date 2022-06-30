p=input();
ret=[]
for i in range(0,len(p),7):
    ret.append(p[i:i+7])
for i in ret:
    # 방법1
    # print(int(i,2))
    # 방법2
    k=1;r=0
    for j in i[::-1]:
        r+=int(j)*k
        k*=2
    print(r)

#################################################################
num ='0000000111100000011000000111100110000110000111100111100111111001100111'
n = len(num)
result = []
for i in range(n//7):
    result.append(int(num[i*7:i*7+7],2))

print(*result)

#######################################################################
number = list(map(int, input()))
tmp = []
for i in range(0, len(number), 7):
    arr = number[i:i+7]
    total = 0
    for j in range(6, -1, -1):
        k = (6-j)
        total += arr[j] * (2**k)
    if i == len(number)-7:
        print(total)
    else:
        print(total, end=', ')

##########################################################
byte = input()
for i in range(len(byte) // 7):
    tmp = byte[i*7:(i+1)*7]
    res = 0
    for e, b in enumerate(tmp[::-1]):
        if b == '1':
            res += pow(2, e)
    print(res)

#################################################
N = input()
for i in range(0, len(N), 7):
    s = N[i:i+7]
    ans = 0
    for j in range(7):
        ans += int(s[j]) * (2 ** (6-j))
    print(ans, end=" ")

##################################################
import sys
sys.stdin = open("input.txt","r")
binary_input = input()
for i in range(1,len(binary_input)//7):
  length7_bin = binary_input[7*(i-1):7*(i)]
  tmp = length7_bin[::-1]
  res = 0
  for i in range(len(tmp)):
    res += 2**i*int(tmp[i])
  print(res)

################################################
arr = list(map(int, input()))
tmp = []
ans = []
for i in range(len(arr)):
    tmp.append(arr[i])
    if i % 7 == 6:
        cnt = 0
        for j in range(1, 8):
            if tmp[-j] == 1:
                cnt += tmp[-j] << j-1
        ans.append(cnt)
        tmp = []
print(*ans)

###################################################
temp = '0000000111100000011000000111100110000110000111100111100111111001100111'
for i in range(0, len(temp), 7):
    print('{}'.format(int(temp[i:7+i],2)))

    ################################################33

bit = input()

for i in range(0, len(bit), 7):
    idx = i
    num = 0
    for j in range(6, -1, -1):
        num += int(bit[idx]) * (2 ** j)
        idx += 1
    print(num)

###########################################################
'''
2진수를 입력받고 7개씩 잘라서 10진수로 출력
'''
#이진수 입력받음
N = input()
for i in range(0,len(N),7):
    print(N[i:i+7])
    print(int(N[i:i+7],2),end=' ')
####################################################
arr = [*map(int, input())]
st = 0
res = 0
temp = []
exponent = 0
cnt = 0

while cnt < len(arr)-1:
    exponent = 0
    if len(arr)-st > 7:
        temp = arr[st:st+7]
        st += 7
    else:
        temp = arr[st:len(arr)]
    for i in range(len(temp)-1, -1, -1):
        if temp[i] == 1:
            res += 2**exponent
        exponent += 1
    cnt += exponent
    print(res, end=' ')
    res = 0
#############################################

import sys
sys.stdin = open('input.txt','r')
#이진수 입력받음
N = input()
for i in range(0,len(N),7):
    num = N[i:i+7]
    ans = 0
    for n in range(len(num)):
        if num[len(num)-n-1] == '1':
            ans += 2**n
            # print(n)
    print(ans,end=' ')
###############################################
n = '0000000111100000011000000111100110000110000111100111100111111001100111'
numbers = []
for i in range(0,len(n) - 6, 7):
    numbers.append([*n[i:i+7]])
reverse_num = []
for num in numbers:
    num = num[::-1]
    reverse_num.append(num)
result = []
for num in reverse_num:
    total = 0
    for i in range(7):
        if num[i] == '1':
            total += 2 ** i
    result.append(total)
print(*result)
