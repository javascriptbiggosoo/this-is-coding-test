# 2.5트 성공, 쩜오인 이유는 두갠데,
# 첫째로 풀이 자체를 내가 떠올리지 못하고 다른 코드를 익혀서 풀었다는 점.
# 나머지 하나는  주석을 보세요
# https://www.acmicpc.net/problem/14888
n = int(input())
nums = list(map(int, input().split()))
덧, 뺄, 곱, 나 = map(int, input().split())

max_num = -1000000000
min_num = 1000000000


def dfs(i, cur):
    global max_num, min_num, 덧, 뺄, 곱, 나
    if i == n:
        max_num = max(max_num, cur)
        min_num = min(min_num, cur)
    if 덧:
        덧 -= 1
        dfs(i + 1, cur + nums[i])
        덧 += 1
    if 뺄:
        뺄 -= 1
        dfs(i + 1, cur - nums[i])
        뺄 += 1
    if 곱:
        곱 -= 1
        dfs(i + 1, cur * nums[i])
        곱 += 1
    if 나:
        나 -= 1
        # dfs(i + 1, cur // nums[i]) // << 음수,양수 나눗셈에서 무조건 아래로쳐냄
        dfs(i + 1, int(cur / nums[i]))  # << 음수일땐 몫을 올림하는데 0을 기준으로 즉, 절댓값 기준으로 내림을 한다고 생각하면 된다.
        나 += 1


dfs(1, nums[0])
print(max_num)
print(min_num)
# 1트, 깔끔하게 실~패 dfs 마스터의 길은 멀고도 험하구나
