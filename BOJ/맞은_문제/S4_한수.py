# 1트 정답, 근데 아무래도 이것보다 나은 풀이가 있을듯
n = int(input())


def 정답자판기(n):
    ans = 0
    for i in range(1, n + 1):  # 1~N
        i = str(i)  # 숫자를 문자열로
        오름 = []
        내림 = []
        for j in range(len(i) - 1):
            차이 = int(i[j]) - int(i[j + 1])
            내림.append(차이)
            차이 = int(i[j + 1]) - int(i[j])
            오름.append(차이)

        if len(i) > 1 and (max(오름) != min(오름) or max(내림) != min(내림)):
            continue
        ans += 1
    print(ans)


정답자판기(n)
