def check(num, notation):
    #현재 비트로 만들어진 10진수를 구해놓는다.
    change_num = int(num, notation)

    idx = len(num)-1
    for i in map(int, num):
        for j in range(notation):
            #자리가 같으면 해볼피룡없이 제껴
            if i == j:
                continue
            #구해놓은 십진수에 원래값비트값을 빼고 새로운 값을 넣어본다.
            tmp = change_num - i * (notation **idx) + j *(notation**idx)
            #그 값이 안들어있다면 추가
            if tmp not in ans:
                ans.append(tmp)
            #들어있다면 리턴
            else:
                return tmp

        idx -= 1



for tc in range(1, int(input())+1):
    num2 = input()
    num3 = input()

    #한비트식 바꾼 10진수를 저장할 리스트
    ans = []

    check(num2, 2)
    print("#{} {}".format(tc, check(num3, 3)))