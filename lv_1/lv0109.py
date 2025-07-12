def solution(a, b):
    answer = 0
    # a,b가 주어질때 a,b 사이에 속한 모든 정수의 합을 리턴

    if a > b:
        a, b = b, a

    for i in range(a, b + 1):
        answer += i
    return answer


print(solution(3, 5))
