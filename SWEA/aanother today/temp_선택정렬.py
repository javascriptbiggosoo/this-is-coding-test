def cleaner(room):
    n = len(room)
    for i in range(0, n - 1):
        start = i
        for j in range(i + 1, n):
            if room[j] < room[start]:
                start = j
        room[i], room[start] = room[start], room[i]
        print(room)


def cleaner(room):
    n = len(room)



my_room = [2, 4, 5, 1, 3]
cleaner(my_room)
print(my_room)