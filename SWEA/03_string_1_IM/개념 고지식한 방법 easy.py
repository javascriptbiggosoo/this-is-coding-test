str1 = "A pattern matching algorithm"
str2 = "rithm"


def 고지식패턴(str1, str2):
    A = len(str1)
    B = len(str2)

    for i in range(A-B+1):  # 철로에서 기차 앞바퀴가 움직일 수 있는 칸 수
        cnt = 0
        for j in range(B):
            if str1[i+j] == str2[j]:
                cnt += 1
            else:
                break
        if cnt == B:
            print("여기부터 일치", i)
            return i
    return -1


tmp = 고지식패턴(str1, str2)
print(tmp)