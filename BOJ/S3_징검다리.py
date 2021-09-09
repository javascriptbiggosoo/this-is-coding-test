# 1트 시간초과
# 등차수열, 이분탐색을 써봅시다.
T = int(input())

for tc in range(T):
    n = int(input())
    curr = 0
    cnt = 1
    while True:
        if curr >= n:
            cnt -= 1
            break
        cnt += 1
        curr += cnt

    print(cnt)


# 2트
