N = int(input())
li = [int(input()) for _ in range(N)]
li.sort()
for i in range(N):
    print(li[i])
