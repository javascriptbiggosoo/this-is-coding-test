"""
ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""
ch_to_int = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 문자 -> int로 맵핑하기 위한 문자열
# 붙어있는입력을 받기
arr = list(ch_to_int)  # 한줄 읽고 리스트로 변환 (문자)
print(arr)
for i in range(len(arr)):
    if arr[i] in ch_to_int:
        print(i + 1, end=" ")
print()
