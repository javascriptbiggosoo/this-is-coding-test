def solution(s):
    최단길이 = len(s)
    # 1개 단위부터 압축 단위를 늘려가며 확인
    for 단위 in range(1, len(s) // 2 + 1):
        압축판 = ""
        도막 = s[0:단위]  # 앞에서부터 단위만큼의 문자열 추출
        count = 1
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for jj in range(단위, len(s), 단위):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if 도막 == s[jj : jj + 단위]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                압축판 += str(count) + 도막 if count >= 2 else 도막
                도막 = s[jj : jj + 단위]  # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        압축판 += str(count) + 도막 if count >= 2 else 도막
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        최단길이 = min(최단길이, len(압축판))

    return 최단길이


solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcabcabcdededededede")
