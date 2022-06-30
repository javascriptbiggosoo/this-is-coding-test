회의수 = int(input())
모든회의 = [list(map(int, input().split())) for _ in range(회의수)]


def 스겜순(회의):
    return (회의[1], 회의[0])


모든회의.sort(key=스겜순)

최대회의 = [모든회의[0]]
for 회의 in 모든회의[1:]:
    if 최대회의[-1][1] <= 회의[0]:
        최대회의.append(회의)

print(len(최대회의))
