def solution(arr, divisor):
    # 나누어 떨어지는 숫자 배열
    # 나누는 숫자로 리스트 내의 값을 나누어떨아지게 만든느 값
    # 그 값들을 오름차순으로 정렬
    answer = []
    arr.sort()
    for x in arr:
        if x % divisor == 0:
            answer.append(x)

    # print(answer)
    if answer:
        return answer
    else:
        return [-1]


print(solution([5, 9, 7, 10], 5))
