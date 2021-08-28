import sys
sys.stdin = open('5204.txt', 'r')
def merge(l, r):
    global big_left
    result = []
    if l[-1] > r[-1]:
        big_left += 1
    while len(l) > 0 and len(r) > 0:
        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
    if len(l) > 0:
        result.extend(l)
    if len(r) > 0:
        result.extend(r)
    return result


def divide(not_sorted):
    if len(not_sorted) <= 1:
        return not_sorted

    mid = len(not_sorted)//2
    left = not_sorted[:mid]
    right = not_sorted[mid:]
    left = divide(left)
    right = divide(right)
    return merge(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))
    big_left = 0
    res = divide(li)
    midd = res[len(res)//2]
    print(f'#{tc} {big_left} {midd}')