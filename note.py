a = [1,2,3,4,5,6,7,8,9]
print(a)

print(a[4])

a = [] * 10     # '빈 리스트' 만들기
print(a)
a = [0] * 10    # '0따리' 리스트
print(a)
b = [1]
print(a+b)
##
##
##
array = [i for i in range(20) if i % 2]
print(array)
array = []
for i in range(20):
    if i%2:
        array.append(i)
print(array)
###
###
###
n = 3
m = 4
array = [[0]*n for _ in range(m)]
print(array)
###
###
###
a = [ 1,3,4]
a.insert(3,5)
print("인덱스 3에 5 추가: ", a)
###
data = {}
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['당근'] = 'carrot'
key_list= data.keys()
print(key_list)
value_list = data.values()
print(value_list)

for key in key_list:
    print(data[key])
###
