def fibo(n):
    if n < 2:
        return n
    elif n >= 2:
        return fibo(n-1) + fibo(n-2)
print(fibo(8))