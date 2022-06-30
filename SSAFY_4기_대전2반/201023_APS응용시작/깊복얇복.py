import copy

old_list = [1,2,3,[1,2,3]]

print("원본 리스트")
print(old_list, id(old_list))


# print("=", 얕은복사)
# new_list1 = old_list
# print(new_list1, id(new_list1))
# old_list.append(5)
# print(new_list1, id(new_list1))

# print("슬라이싱 , 깊은복사")
# new_list2 = old_list[:]
# print(new_list2, id(new_list2))
# old_list.append(5)
# print(new_list2, id(new_list2))

# print("extend, 깊은복사")
# new_list3 = []
# new_list3.extend(old_list)
# print(new_list3, id(new_list3))
# old_list.append(5)
# print(new_list3, id(new_list3))

# print("list(), 깊은복사")
# new_list4 = list(old_list)
# print(new_list4, id(new_list4))
# old_list.append(5)
# print(new_list4, id(new_list4))

# print("append, 얕은 복사긴한데 한칸더들어감")
# new_list5 = []
# new_list5.append(old_list)
# print(new_list5, id(new_list5))
# old_list.append(5)
# print(new_list5, id(new_list5))
# #
# print("+, 깊은복사")
# new_list6 = []
# new_list6 += old_list
# print(new_list6, id(new_list6))
# old_list.append(5)
# print(new_list6, id(new_list6))

# print("copy활용, 2중포문 안에서 얕은복사 ")
#이예제는 잘 맞지 않음
# new_list7 = copy.copy(old_list)
# print(new_list7, id(new_list7))
# old_list.append(5)
# print(new_list7, id(new_list7))

# print("deepcopy활용, 깊은복사 ")
# new_list8 = copy.deepcopy(old_list)
# print(new_list8, id(new_list8))
# old_list.append(5)
# print(new_list8, id(new_list8))

print("리스트함축, 깊은복사 ")
new_list8 = [_ for _ in old_list]
print(new_list8, id(new_list8))
old_list.append(5)
print(new_list8, id(new_list8))

#공식문서
# https://docs.python.org/ko/3/library/copy.html
