# 1트 n이 나누어질때마다 2부터 올라가면서 소수로 나눠지면 나누게 해봄
# 시간초과

# n = int(input())

# while n != 1:
#     for i in range(2, n + 1):  # 소수를 찾을거야
#         소수 = True
#         if i != 2:
#             for j in range(2, i):
#                 if i % j == 0:
#                     소수 = False
#                     break

#         if 소수:
#             if n % i == 0 and n != 1:
#                 n //= i
#                 print(i)
#                 break

# 2트, n이 가진 모든 소수를 리스트에 박아넣고 n이 나눠질때마다 소수 리스트를 순회하면서 나눠지는지 확인
# 시간초과
n = int(input())
소수 = []

for i in range(2, n // 2):  # 소수를 찾을거야
    if n % i == 0:
        소수.append(i)

while n != i:
    for i in range(len(소수)):
        if 소수[i] > n:
            break
        if n % 소수[i] == 0:
            n //= 소수[i]
            print(소수[i])
            break
