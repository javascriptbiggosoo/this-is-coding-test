def merge(left, right):
    global ans

    # 미리 합한 크기만큼
    result = [0] * (len(left) + len(right))
    idx = li = ri = 0

    if left[-1] > right[-1]: ans += 1

    while len(left) > li and len(right) > ri:
        if left[li] <= right[ri]:
            result[idx] = left[li]
            li += 1
            idx += 1
        else:
            result[idx] = right[ri]
            ri += 1
            idx += 1

    while len(left) > li:
        result[idx] = left[li]
        li += 1
        idx += 1

    while len(right) > ri:
        result[idx] = right[ri]
        ri += 1
        idx += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1: return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))  # 정렬배열입력

    ans = 0

    nums = merge_sort(nums)
    print("#{} {} {}".format(tc, nums[N // 2], ans))
