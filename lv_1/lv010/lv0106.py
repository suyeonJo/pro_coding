def solution(x, n):
    # x씩 늘어나는 n개의 원소를 갖는 리스트를 리턴
    # [2,4,6,8,10]
    cnt = x
    answer = []

    for i in range(n):
        answer.append(x)
        x += cnt

    return answer


print(solution(2, 5))
