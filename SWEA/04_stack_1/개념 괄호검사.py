# 괄호검사

# 1.왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야한다.
# 2.같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
# 3.괄호 사이에는 포함 관계가 존재한다.

# input 값
# 3
# {()}{[]}
# ([)](())
# (][())


def check(bracket):
    # 인자로 넘어온 괄호들을 순회하면서 검사한다.
    # 여는 괄호라면 무조건 push
    # 닫는 괄호라면 일단 pop 하고 스택에 top 위치와 비교 제짝이면 continue
    # 제짝이 아니면 False
    # 끝까지 순회했을때 스택의 길이가 0이 아니라면 False

    # 언럭키 테트리스
    stack = []

    for i in range(len(bracket)):
        if bracket[i] == '(' or bracket[i] == '{' or bracket[i] == '[':
            stack.append(bracket[i])        # 여는거면 일단 넣어야지 아ㅋㅋ
        elif bracket[i] == ')' or bracket[i] == '}' or bracket[i] == ']':
            if len(stack) == 0:
                return False
            tmp = stack.pop()

            if bracket[i] == ')' and tmp == '(':
                continue
            elif bracket[i] == '}' and tmp == '{':
                continue
            elif bracket[i] == ']' and tmp == '[':
                continue

            return False
    if len(stack) > 0:
        return False

    return True


for _ in range(int(input())):
    bracket = input()

    print(check(bracket))