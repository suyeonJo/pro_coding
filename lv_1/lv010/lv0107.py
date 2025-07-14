def solution(n):
    # 자연수 n이 매개변수 n을 x로 나눈 나머지가 1이 되도록하는 가장작은 자연수
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            return answer
    return answer


# print(solution(10))
