import sys

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    arr = [a, b, c]
    if a == 0 and b == 0 and c == 0:
        break
    if sorted(arr)[2] ** 2 == sorted(arr)[1] ** 2 + sorted(arr)[0] ** 2:
        print("right")
    else:
        print("wrong")
