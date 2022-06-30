for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    ans = 0

    for key in B:
        l = 0
        r = N - 1

        flag = 0
        while l <= r:
            mid = (l + r) // 2

            if key == A[mid]:
                ans += 1
                break
            # 오른쪽이동
            elif key > A[mid]:
                l = mid + 1
                if flag == 1: break
                flag = 1
            # 왼쪽이동
            else:
                r = mid - 1
                if flag == -1: break
                flag = -1

    print("#{} {}".format(tc, ans))
