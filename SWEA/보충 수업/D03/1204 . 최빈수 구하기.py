import sys
sys.stdin = open("1204.txt", "r")

T = int(input())
for tc in range(1,T+1):
    int(input())
    arr = list(map(int,input().split()))
    # print(arr)
    # 각 학생의 점수는 0점 이상 100점 이하 => 일정 범위의 정수 => 카운팅 배열을 이용해서 집계
    count = [0] * 101
    for score in arr:
        # print(score)
        count[score] +=1    #해당 점수 => 인덱스 => 인덱스의 값을 하나 증가
    # print(count)
    # 그 중 가장 큰 값을 찾기 => 그때의 인덱스가 점수
    max = 0
    maxIdx = 0
    for i in range(len(count)):
        if max < count[i] or (max == count[i] and maxIdx < i):
            max = count[i]
            maxIdx = i
    print("#{} {}".format(tc, maxIdx))
