# https://www.acmicpc.net/problem/18406
# 1트, 성공
점수 = input()
중앙 = len(점수) // 2
앞 = 점수[:중앙]
뒤 = 점수[중앙:]
앞총점 = []
뒷총점 = []
for i in range(중앙):
    앞총점.append(int(앞[i]))
    뒷총점.append(int(뒤[i]))

if sum(앞총점) == sum(뒷총점):
    print("LUCKY")
else:
    print("READY")
