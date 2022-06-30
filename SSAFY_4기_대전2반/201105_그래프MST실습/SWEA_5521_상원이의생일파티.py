for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]

    for i in range(M):
        A,B = map(int, input().split())

        G[A].append(B)
        G[B].append(A)

    ans = len(G[1])
    visit = set([1] + G[1])
    #상원이랑 바로 친한친구
    for a in G[1]:
        #친한친구의 친한친구 (친친친친)
        for b in G[a]:
            if b in visit: continue
            ans += 1
            visit.add(b)

    print("#{} {}".format(tc, ans))
