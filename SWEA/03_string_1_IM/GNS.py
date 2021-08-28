num_list = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]
num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

T = int(input())

for tc in range(1, T + 1):
    a, b = input().split()

    arr = list(input().split())

    cnt = [0] * 10
    for key in arr:                 # 받은 글자 뭉치에서 하나씩 꺼낸다
        cnt[num_dict[key]] += 1     # num_dict 에서 글자뭉치에 대응되는 숫자를 찾아내고 리스트의 해당 칸에 숫자를 증가시켜준다

    print("#{}".format(tc))

    for i in range(10):
        print(num_list[i] * cnt[i], end="")     # 증가된 숫자만큼 다시 칸에 대응되는 글자뭉치를 뱉어냄 ㅋㄷ
    print()