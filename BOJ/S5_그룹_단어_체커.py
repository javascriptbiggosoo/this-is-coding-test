N = int(input())

target = [input() for _ in range(N)]

group = N
for i in range(N):  # 단어
    this_turn = target[i]
    len_this_turn = len(this_turn)
    bucket = []
    for j in range(len_this_turn):  # 글자
        if len(bucket) > 0 and bucket[-1] != this_turn[j]:
            if this_turn[j] in bucket:
                group -= 1
                break
        bucket.append(this_turn[j])

print(group)
