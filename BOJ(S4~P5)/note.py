# 1트, 팩토리얼을 재귀로 구현하면서 런타임 에러뜸, 반복으로 수정 후 정답

n = int(input())

fact = 1
for i in range(1, n + 1):
    fact *= i


target = str(fact)
cnt = 0
for i in range(len(target)):
    # print(cnt)
    if target[-(i + 1)] == "0":
        cnt += 1
    else:
        break

print(cnt)
