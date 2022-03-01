def solution(n, lost, reserve):
    s = set(lost) & set(reserve)  # &연산자로 교집합 생성
    l = set(lost) - s  # 차집합
    r = set(reserve) - s

    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)

    return n - len(l)
