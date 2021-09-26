# https://www.acmicpc.net/problem/1439
# 1트, 성공

s = input()
압축 = []
압축.append(s[0])
for i in range(1, len(s)):
    if 압축[-1] != s[i]:
        압축.append(s[i])  # 0001100 ->010

ans = len(압축) // 2  # 압축의 길이가 짝수인 경우 한 번 뒤집으면 2개씩 줄어듬, 홀수인 경우 한 번 뒤집고 나면 짝수가 됨

print(ans)
