# 해시를 이용하면 시간복잡도 O(N)인데 정렬을 이용해서 풀면 아무리 못해도 O(NlogN)이 소요된다.


def solution(participant, completion):
    participant.sort()
    completion.sort()

    answer = participant[-1]

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer
