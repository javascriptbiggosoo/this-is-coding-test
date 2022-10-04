p=input();ret=[];tmp=''
c={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
for i in p:tmp+=c[i]
for i in range(0,len(tmp),7):ret.append(tmp[i:i+7])
for i in ret:
    # 방법1
    # print(int(i,2))
    # 방법2
    k=1;r=0
    for j in i[::-1]:r+=int(j)*k;k*=2
    print(r)

################################################

# 01D06079861D79F99F
# 0F97A3
b_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
          'D': '1101', 'E': '1110', 'F': '1111'}


def change(num):
    if len(num) < 7:
        num = '0' * (7 - len(num)) + num
    idx = 0
    ans = 0
    print(num)
    for i in range(6, -1, -1):
        ans += int(num[idx]) * (2 ** i)
        idx += 1
    print(ans)


line = input()

binary = ""
for i in line:
    binary += b_dict[i]

for i in range(0, len(binary), 7):
    change(binary[i:i + 7])

##################################################

a = '01D06079861D79F99F'
b = '0F97A3'
def cal(i):
    ret = 0
    for k in range(len(i)):
        tmp = pow(2, k)
        if i[::-1][k] == '1':
            ret += tmp
    return ret
def bit(i):
    ret = ''
    for j in range(3, -1, -1):
        ret += '1' if i & (1 << j) else '0'
    return ret
res = ''
for k in a:
    res += bit(int(k, 16))
for i in range(len(res) // 7 + 1):
    print(cal(res[i * 7:(i + 1) * 7]))
########################################
num_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
N = input()
s = ''
for i in range(len(N)):
    if N[i] in num_dict.keys():
        a = bin(num_dict[N[i]])[2:6]
        s += a
    else:
        b = bin(int(N[i]))
        if int(N[i]) >= 8:
            s += b[2:6]
        elif int(N[i]) >= 4:
            s += '0' + b[2:5]
        elif int(N[i]) >= 2:
            s += '00' + b[2:4]
        else:
            s += '000' + b[2]

for j in range(0, len(s), 7):
    c = s[j:j+7]
    ans = int(c, 2)
    print(ans, end=" ")

####################################################

def bin(a):
    sub = ''
    if a ==0:
        return '0000'
    while a > 1:
        sub+= str(a % 2)
        a = a//2
    sub += '1'
    if len(sub) < 4:
        sub += '0'*(4-len(sub))
    return sub[::-1]

number = ['A', 'B', 'C', 'D', 'E', 'F']
temp = '01D06079861D79F99F'
b = ''
for t in temp:
    if t.isdigit():
        b += bin(int(t))
    else:
        b += bin(number.index(t)+10)
result =[]
for i in range(len(b)//7+1):
    result.append(int(b[i*7:i*7+7],2))
print(*result)

#################################################
def tobin(x):
    res,num='',int(x,16)
    while num > 0:
        res = str(num % 2) + res
        num //= 2
    while len(res)<4:
        res='0'+res
    return res
hex_num='01D06079861D79F99F'
bin_num=''
for num in hex_num:
    bin_num+=tobin(num)
for i in range(0,len(bin_num),7):
    print(int(bin_num[i:i+7],2))
##################################################
N = input()
s = ''
for i in range(len(N)):
    b = int(N[i], 16)
    a = bin(b)
    if b >= 8:
        s += a[2:6]
    elif b >= 4:
        s += '0' + a[2:5]
    elif b >= 2:
        s += '00' + a[2:4]
    else:
        s += '000' + a[2]

for j in range(0, len(s), 7):
    c = s[j:j+7]
    ans = int(c, 2)
    print(ans, end=" ")

################################################
def decimal_to_binary(n):
  result = []
  while n:
    mod = n%2
    n = n//2
    result += [str(mod)]
  result = ['0'] * (4-len(result)) + result[::-1]
  return ''.join(result)

myinput = '01D06079861D79F99F'
binray = ''
for i in myinput:
  binray+=decimal_to_binary(int(i,16))
for i in range(0,len(binray),7):
  print(int(binray[i:i+7],2))

#####################################################
N = input()
s = ''
for i in range(len(N)):
    b = int(N[i], 16)
    t = 8
    while t >= 1:
        s += str(b // t)
        b = b % t
        t //= 2

for j in range(0, len(s), 7):
    c = s[j:j+7]
    ans = int(c, 2)
    print(ans, end=" ")
#########################################

num = input()
n = len(num)
alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
result = ''
for i in range(n):
    if num[i].isdigit():
        N = int(num[i])
    else:
        N = alphabet.index(num[i]) + 10
    r = ['0', '0', '0', '0']
    idx = 3
    while idx >= 0:
        r[idx] = str(N % 2)
        N = N // 2
        idx -= 1
    for j in range(len(r)):
        result += r[j]

ans = []
for i in range(0, len(result) - 7, 7):
    number = result[i:i + 7]
    total = 0
    for j in range(7):
        if number[j] == '1':
            total += 2 ** (6 - j)
    ans.append(total)

p = len(result) % 7
total = 0
for i in range(p):
    if result[len(result) - i - 1] == '1':
        total += 2 ** i
ans.append(total)
print(*ans)

###############################################
arr = ['0','F','9','7','A','3']
dict = {'0' : '0000' , '1' : '0001', '2' : '0010' , '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
        'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'}
binstr = ''
for each in arr:
    binstr += dict[each]
for i in range(0,len(binstr),7):
    num = 0
    v = 1
    for each in binstr[i:i+7][::-1]:
        if each == '1':
            num += v
        v *= 2
    print(num)
##########################################################
hexa = list(input())            # 16진수 string을 list로 한 개씩 저장
binstr = ''                     # 2진수로 변환된 숫자를 저장할 string
ans = []                        # 다시 10진수로 변환한 값 담을 array

for h in hexa:
    h = int('0x' + h, 16)       # 문자로 받은 h값을 16진수로 변환
    h = format(h, 'b')          # 16진수 h를 0b제외한 2진수 문자열로 받기
    if len(h) < 4:              # h의 길이가 4보다 작을 경우 (h가 0 ~ 7)
        h = '0' * (4 - len(h)) + h  # 0 추가해서 길이 4로 맞춰줌
    binstr += h

for i in range(0, len(binstr), 7):
    tmp = binstr[i:i + 7]       # 7씩 자른 값 tmp에 임시저장
    ans.append(int('0b' + tmp, 2))

print(*ans)
################################################
'''
01D06079861D79F99F
'''

def binary(num):
    global result,cnt
    if num == 0:
        return result
    result[3-cnt] = str(num%2)
    num //= 2
    cnt+=1
    binary(num)

alpha = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
bit = input()
#16진수는 각자리수를 2진수로 바꿔주면 2진수로 바뀜!!
nums = ''
for b in bit:
    result = ['0']*4
    cnt = 0
    #알파벳은 수로 변환
    if b.isalpha():
        for a in alpha:
            val = alpha[b]
        binary(val)
        nums += ''.join(result)
        continue
    binary(int(b))
    nums += ''.join(result)
for n in range(0,len(nums),7):
    words = nums[n:n+7]
    temp = 0
    for w in range(len(words)):
        word = words[len(words)-w-1]
        if int(word):
            temp += 2**w
    print(temp,end=' ')
###########################################
# 01D06079861D79F99F
# 2진수 변경 함수(순서가 반대)
def binary(x):
    bin = []
    while x:
        bin.append(x % 2)
        x = x // 2
    return bin

arr = list(input())
tmp = ['A', 'B', 'C', 'D', 'E', 'F']
# 16진수 인트형태로 변환
for i in range(len(arr)):
    if arr[i] in tmp:
        arr[i] = tmp.index(arr[i]) + 10
    else:
        arr[i] = int(arr[i])
# 16진수 -> 2진수 / 4비트씩 맞춰서 ans에 추가
ans = []
for i in range(len(arr)):
    lis = binary(arr[i])
    if len(lis) != 4:
        while len(lis) < 4:
            lis.append(0)
    for j in range(len(lis)-1, -1, -1):
        ans.append(lis[j])
# 2진수 -> 10진수
for i in range(0, len(ans), 7):
    answer = ans[i:i+7]
    cnt = 0
    for j in range(1, len(answer)+1):
        if answer[-j] == 1:
            cnt += answer[-j] << j-1
    if i >= len(ans) - 7:
        print(cnt)
    else:
        print(cnt, end=', ')
    ################################################################

num = 0x01D06079861D79F99F
binay_num = bin(num)[2:]
temp = (len(str(num))-2) * 4 - len(binay_num)
binay_num = '0' * temp + binay_num
for i in range(0, len(binay_num), 7):
    print(int(binay_num[i:i+7], 2))
###########################################
n = input()
Bin = ''
for i in range(len(n)):
    hx = int(n[i], 16)
    bin = str(format(hx, 'b'))

    if len(bin) < 4:
        a = '0'*(4-len(bin))
        bin = a+bin
    Bin += bin



save = []
for i in range(0, len(Bin), 7):
    tmp = Bin[i:i+7]
    total = 0
    for j in range(len(tmp)):
        if tmp[len(tmp)-1-j] == '1':
            total += 2**j
    save.append(total)

for i in range(len(save)):
    if i == len(save)-1:
        print(save[i])
    else:
        print(save[i], end=', ')
    ########################################