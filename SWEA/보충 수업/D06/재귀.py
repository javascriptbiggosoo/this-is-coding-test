# 재귀 함수
# 자기 자신을 호출하는 함수

# def func():     #함수를 정의
#     print("hello")
#     func()  #나 자신을 호출
# func()
"""
위의 코드를 실행하면 무한루프 발생
- 무한 루프에 안빠지려면?
    : 매개변수를 하나 받음
    : 재귀 호출이 일어날때마다 매개변수가 변하도록 설정
    : 재귀 함수에서 매개변수의 값을 이용해 조건을 설정하고
      일정조건을 만족하면 더이상 함수 호출을 안하도록 함(리턴 함)
"""


def func(k):  # 함수를 정의
    if k >= 10:
        return
    print("hello", k)
    func(k + 1)  # 나 자신을 호출


func(0)
"""
재귀 함수의 구조
- 기본파트 (base part)
    : 적어도 하나의 재귀에 빠지지 않는 경우가 있어야함.
    : 조건식을 만족하면 리턴하게(더이상 호출안하게)
- 유도파트 (recursion part)
    : 자기 자신을 호출하는 부분
    : 재귀를 반복하다보면 결국 base case에 수렴하도록 해야함
"""
# 1~5까지의 합을 구하는 함수 (재귀)
# def sum(k,total):
#     if k <= 0 :
#         print(total)
#         return
#     sum(k-1, total+k)
# sum(5,0)


def sum2(k):
    if k == 0:
        return 0
    return k + sum2(k - 1)


result = sum2(5)
print(result)
