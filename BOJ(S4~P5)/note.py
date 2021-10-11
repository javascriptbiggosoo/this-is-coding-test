n = int(input())
ans = 0
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    ans = 1
print(ans)
