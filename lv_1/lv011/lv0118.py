def solution(num):
    # 콜라츠 추측
    # 주어진 수가 1이 될때까지 다음작업을 반복
    # 모든 수를 1로 만들수 있다는 추측
    # 짝수는 2로 나누기
    # 홀수는 3을 곱하고 1을 더하기
    # 값이 1이 될때까지 반복
    # 총 몇번 반복 하는 지!
    if num == 1:
        return 0

    answer = 0

    while num != 1:
        if answer >= 500:
            return -1

        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1

        answer += 1

    return answer


print(solution(626331))
