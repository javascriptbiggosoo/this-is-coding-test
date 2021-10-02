찾는곳, 찾을것 = map(int, input().split())

대충사전 = {}
for i in range(찾는곳):
    s, p = input().split()
    대충사전[s] = p
for i in range(찾을것):
    s = input()
    print(대충사전[s])
