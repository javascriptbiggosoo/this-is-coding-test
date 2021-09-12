# 1트
# for 문을 range()말고 에너미컨트롤러로 하는게 더 편했을듯
# 행열에 값을 주고 초기화하는것 보다 답안 예시처럼 새행열 변수를 만들었으면 초기화는 필요 없었을듯

position = input()
행 = int(position[1])
열 = int(ord(position[0]) - 96)

에너미컨트롤러 = [[2, 1], [1, 2], [-2, 1], [1, -2], [2, -1], [-1, 2], [-2, -1], [-1, -2]]
ans = 0
for i in range(8):
    행 += 에너미컨트롤러[i][0]
    열 += 에너미컨트롤러[i][1]
    if 행 > 0 and 행 <= 8 and 열 > 0 and 열 <= 8:
        ans += 1
    행 = int(position[1])
    열 = int(ord(position[0]) - 96)

print(ans)
