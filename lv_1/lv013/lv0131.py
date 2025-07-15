def solution(arr):
    # 같은 숫자는 싫어
    # 배열 arr이 주어진다. 0~9 숫자
    # 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
    # 단 제거 된후 남은 수들을 반환할떄는 순서유지
    answer = []

    for x in arr:
        if not answer:
            answer.append(x)
            continue

        if answer[-1] == x:
            continue
        else:
            answer.append(x)

    return answer


# if not answer: 로 첫 번째 요소 처리
# answer[-1] 로 마지막 요소와 비교
# continue 사용으로 조건별 분기 명확화


print(solution([1, 1, 3, 3, 0, 1, 1]))
