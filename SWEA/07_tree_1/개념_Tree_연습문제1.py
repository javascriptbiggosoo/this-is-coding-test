# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# 이거 이해하면 9/9 중위순회 문제 쉽게 풀 수 있을 것 같다

N = int(input())
info = list(map(int, input().split()))
tree = [0] * 100

for i in range(0, len(info), 2):
    p = info[i]
    c = info[i + 1]

    if p not in tree:
        idx = -1
    else:
        idx = tree.index(p)

    if idx == -1:
        tree[1] = p
        tree[2] = c
    else:
        # 왼쪽자식이 비었으면 거기
        if tree[idx * 2] == 0:
            tree[idx * 2] = c
        # 아니라면 오른쪽
        else:
            tree[idx * 2 + 1] = c


# 전위
def pre_order(index):
    print(tree[index], end=" ")
    if tree[index * 2] != 0:
        pre_order(index * 2)
    if tree[index * 2 + 1] != 0:
        pre_order(index * 2 + 1)


# 중위 신민호
def in_order(index):
    if tree[index * 2] != 0:
        in_order(index * 2)
    print(tree[index], end=" ")
    if tree[index * 2 + 1] != 0:
        in_order(index * 2 + 1)


# 후위
def post_order(index):
    if tree[index * 2] != 0:
        post_order(index * 2)
    if tree[index * 2 + 1] != 0:
        post_order(index * 2 + 1)
    print(tree[index], end=" ")

pre_order(1)
print()
in_order(1)
print()
post_order(1)

# 라이브 버전
# def preorder(node):
#     if node:
#         print(node, end=" ")
#         preorder(tree[node][0])
#         preorder(tree[node][1])
#
#
# V = int(input())  # 정점
# E = V - 1  # 간선
#
# tree = [[0] * 3 for _ in range(V + 1)]  # 14 * 3
# temp = list(map(int, input().split()))
# # 트리에 저장
#
# for i in range(E):
#     p, c = temp[i * 2], temp[i * 2 + 1]
#     if tree[p][0] == 0:
#         tree[p][0] = c  # left
#     else:
#         tree[p][1] = c  # right
#     tree[c][2] = p  # parent
#
# for t in tree:
#     print(*t)
#
# preorder(1)
