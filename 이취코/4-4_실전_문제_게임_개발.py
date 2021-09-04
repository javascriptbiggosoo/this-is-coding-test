# 힘겹게 제출했는데 일단 모양이 잘 나오긴함
# 코드 자체도 아직 덜 깔끔하고
# 시험삼아 만든
# 5 5
# 1 1 0
# 1 1 1 1 1
# 1 0 0 1 1
# 1 0 1 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# 입력을 넣어도 되긴하는데 진짜 에러 없는 코드인지 아직 몰겠덩 ㅋㅋ

import pprint

# 에너미 컨트롤러
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
A, B, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
out = 1
while out:
    # 1단계
    arr[A][B] = 2   # 방문표시
    for _ in range(4):
        if d == 0:  # 좌회전
            d = 3
        else:
            d -= 1
        if arr[A+dr[d]][B+dc[d]] == 0:    # 회전한 곳이 미개척지인가요?
            # 2단계
            A = A + dr[d]   # 앞으로 갑시다.
            B = B + dc[d]
            break

    if arr[A][B] == 0:   # 육지면 계속 전진, 외곽이 바다라서 인덱스 에러는 고려하지 않아도 됨
        continue
    else:                # 길이 아니면 한 칸씩 돌아가
        current_d = d
        while arr[A][B] != 1 and current_d == d:    # 갈 곳 생길 때 까지 한바퀴 돌고 문워크
            arr[A][B] = 2
            A = A - dr[d]
            B = B - dc[d]
            if arr[A][B] == 1:
                out = 0
                break
            # 좌회전 한 곳에 0이 있으면 전진하고 아니면 다시 좌회전 하는 구문(네번 돌고 없으면 다시 뒤로 가겠지)
            for _ in range(4):
                if d == 0:  # 좌회전
                    d = 3
                else:
                    d -= 1
                if arr[A][B] == 0:    # 회전한 곳이 미개척지인가요?
                    break
        if current_d != d:
            A = A + dr[d]   # 앞으로 갑시다.
            B = B + dc[d]
    pprint.pprint(arr)
