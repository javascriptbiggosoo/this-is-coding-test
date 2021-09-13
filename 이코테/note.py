# 팩토리얼을 만드러보장
def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


print(fact(5))
fact(3)
