def solution(a, b):
    # 내적
    # 길이가 같은 1차원 정수배열 a,b
    # 각 인덱스의 값끼리 곱해서 더한 값을 리턴하면된다

    answer = 0

    for i in range(len(a)):
        answer += (a[i] * b[i])

    return answer


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
