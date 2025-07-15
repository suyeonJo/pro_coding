def solution(n):
    # 수박수박수박
    # n이 4이면 수박수박을 리턴
    # 3이면 수박수 리턴

    answer = ''
    a = "수"
    b = "박"

    for i in range(n):
        if not answer:
            answer += a
            continue

        if answer[-1] == a:
            answer += b
        else:
            answer += a
    return answer


# print(solution(6))
# 1. 인덱스 활용 (가장 직관적)
# def solution(n):
#     answer = ''
#     for i in range(n):
#         if i % 2 == 0:
#             answer += "수"
#         else:
#             answer += "박"
#     return answer
