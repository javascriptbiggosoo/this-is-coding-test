cro = input()
res = len(cro)

li = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
for i in range(len(li)):
    res -= cro.count(li[i])

res -= cro.count("dz=")
print(res)
