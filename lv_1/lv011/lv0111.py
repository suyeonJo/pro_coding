def solution(n):
    answer = 0
    # 정수로 받아서 리스트화 한 다음  큰것부터 작은것으로 정렬
    res = []

    for x in str(n):
        res.append(x)
    # print(res)
    answer = ''.join(sorted(res, reverse=True))
    # print(type(answer))

    return int(answer)


print(solution(118372))
