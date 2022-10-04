def quick_sort(arr, l, r):
    if l < r:
        p = hoare_partition(arr, l, r)
        quick_sort(arr, l, p-1)
        quick_sort(arr, p+1, r)

def hoare_partition(arr, l , r):
    pivot = arr[l]
    i = l
    j = r

    while i<=j:
        while i<= j and arr[i] <= pivot: i+=1
        while i <= j and arr[j]>= pivot: j-=1

        if i <j :
            arr[i], arr[j]  = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j

def lomuto_partition(arr, l, r):
    pivot = arr[r]
    i = l - 1

    for j in range(l, r):
        if arr[j] <= pivot:
            i +=1
            arr[i], arr[j] = arr[j] , arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))


    quick_sort(nums, 0, N-1)

    print("#{} {}".format(tc, nums[N//2]))