a = [] * 10  # '빈 리스트' 만들기
print(a)
a = [0] * 10  # '0따리' 리스트
print(a)
b = [1]
print(a + b)
print("0########")
array = [i for i in range(20) if i % 2]
print(array)
array = []
for i in range(20):
    if i % 2:
        array.append(i)
print(array)
print("1########")
n = 3
m = 4
array = [[0] * n for _ in range(m)]
print(array)
print("2########")
a = [1, 3, 4]
a.insert(3, 5)
print("인덱스 3에 5 추가: ", a)
print("3########")

data = {}
data["사과"] = "apple"
data["바나나"] = "banana"
data["당근"] = "carrot"
key_list = data.keys()
print(key_list)
value_list = data.values()
print(value_list)

for key in key_list:
    print(data[key])
print("4########")
print(1, end=" ")
print(2, end=" ")
print(3)

print("5########")


print("6########")
print("7########")
