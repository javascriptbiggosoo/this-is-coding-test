N = 3
arr = [1, 2, 3]
sel = [0] * N


def powerset(idx):
    if N == idx:
        print(sel, ': ', end=' ')
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return

    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)


powerset(0)
