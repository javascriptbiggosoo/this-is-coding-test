while True:
    문자열 = input()
    if 문자열 == ".":
        break

    스택 = []

    for i in 문자열:
        if i == "[":
            스택.append(i)
            continue
        if i == "(":
            스택.append(i)
            continue

        if i == "]":
            if len(스택):
                if 스택[-1] == "(":
                    스택.append(False)
                    break
                else:
                    스택.pop()
                    continue
            else:
                스택.append(False)
                break

        if i == ")":
            if len(스택):
                if 스택[-1] == "[":
                    스택.append(False)
                    break
                else:
                    스택.pop()
                    continue
            else:
                스택.append(False)
                break

    if len(스택):
        print("no")
    else:
        print("yes")
