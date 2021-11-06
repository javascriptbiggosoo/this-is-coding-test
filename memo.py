print("0########")

array = [i for i in range(20) if i % 2]
print(array)
array = []
for i in range(20):
    if i % 2:
        array.append(i)
print(array)
print("조합 만들기:")

print("sort(key=lambda x:x[0])")


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

print("5########")


print("6########")
print("7########")
