# 정말로 풀기만 풀어냄

import sys

sys.stdin = open("5208.txt", "r")

T = int(input())
for tc in range(1, 1 + T):
    li = list(map(int, input().split()))
    N = li[0]
    Mi = li[1:]

    idx = 0  # 현재 서 있는 징검다리
    jump = -1  # 점프 횟수
    while len(Mi) > idx:
        power = Mi[idx]  # 점프력
        potential = idx + power  # 현재 갈 수 있는 최대 지점
        if potential >= len(Mi):
            jump += 1
            idx = potential
        else:
            p = []
            for i in range(power):
                if (
                    len(Mi) > potential - i >= 0
                    and potential - i + Mi[potential - i] > potential
                ):
                    if len(p) and potential - i + Mi[potential - i] > p[1]:
                        p.pop()
                        p.pop()
                    p.append(potential - i)
                    p.append(potential - i + Mi[potential - i])
            idx = p.pop(0)
            jump += 1

    print(f"#{tc} {jump}")
