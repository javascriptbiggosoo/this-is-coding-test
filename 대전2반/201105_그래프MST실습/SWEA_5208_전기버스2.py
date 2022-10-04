def check(my, cnt):
    global ans
    #가지치기
    if cnt > ans:
        return

    if my >= bus_stop[0]:
        ans = min(ans, cnt)
        return

    for i in range(my + bus_stop[my], my, -1):
        check(i, cnt+1)


for tc in range(1, int(input())+1):
    bus_stop = list(map(int, input().split()))
    ans = 987654321

    check(1, -1)

    print("#{} {}".format(tc, ans))