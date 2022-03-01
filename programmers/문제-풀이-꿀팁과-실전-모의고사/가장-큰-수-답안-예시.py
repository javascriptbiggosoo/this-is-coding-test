def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)   # 자릿수 제한에 근거해서, 숫자를 이어 붙이다보면 4번째 자리 안에서 대소가 결정이 된다
    if numbers[0] == '0':
        answer = '0'    # 이 예외처리가 좀 지저분한게 00000이 입력으로 오면 0으로 취급해야한다는걸 고려해야함
    else:
        answer = ''.join(numbers)
    return answer
