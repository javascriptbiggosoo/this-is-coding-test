n = int(input())
p = list(map(int, input().split()))
p.sort()
curr = 0
res = 0
for i in p:
    curr += i
    res += curr
print(res)
