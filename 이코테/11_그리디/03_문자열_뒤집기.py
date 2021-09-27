# https://www.acmicpc.net/problem/1439
# 1트, 성공, 교재 답안 예시를 봤는데.. 놀랍게도 내 풀이가 더 낫다. 몇 번을 봐도

s = input()
압축 = []
압축.append(s[0])
for i in range(1, len(s)):
    if 압축[-1] != s[i]:
        압축.append(s[i])  # 0001100 -> 010(0과 1이 번갈아가며 반복하는 모양)

ans = len(압축) // 2  # 한 번 뒤집을 때마다 2개씩 줄어듬. 010101 -> 0101, 0101010 -> 01010
print(ans)
