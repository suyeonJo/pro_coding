def solution(n):
    answer = 0
    # 정수제곱근 판별, 임의의 양의 정수 n 에 대해
    # n 이 어떤 양의 정수 x 의 제곱인지 아닌지 판단
    # n 이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴 아니면 -1
    # 실수와 정수의 값을 비교하는것이 포인트

    tmp = n ** 0.5
    # print(tmp)
    if tmp == int(tmp):
        answer = (tmp + 1) ** 2
        return int(answer)
    else:
        return -1

# print(solution(121))
