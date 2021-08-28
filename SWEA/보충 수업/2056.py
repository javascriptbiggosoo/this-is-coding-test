'''
5
22220228
20150002
01010101
20140230
11111111
'''
day = [0,31,28,31,30,31,30,31,31,30,31,30,31]   #각 월에 해당하는 일수를 리스트로 저장
T = int(input())
for tc in range(1,T+1):
    arr = input()
    y,m,d = arr[0:4],arr[4:6],arr[6:9]  #입력받은 정보를 잘라서 저장
    # print(y,m,d)
    if int(m) > 12 or int(m) <= 0:  #월이 0이하이거나 12를 초과하면 -1 출력하고 이번 턴은 끝내기
        print("#{} -1".format(tc))
        continue    #continue는 지금 하고 있는 턴을 종료하고 다시 반복문 처음으로 감
    if 0 <= int(d) > day[int(m)]:    #일이 0보다 같거나 작거나 기준일보다 크면 -1 출력하고 이번턴 끝냄
        print("#{} -1".format(tc))
        continue
    print("#{} {}/{}/{}".format(tc, y,m,d)) #위에 테스트를 다 통과했다면 괜찮은 거니까 출력!