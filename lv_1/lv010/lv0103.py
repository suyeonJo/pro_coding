def solution(n):
    # n = 12345
    answer = []
    new_n = str(n)[::-1]

    # print(new_n)

    for x in new_n:
        answer.append(int(x))
    return answer

# solution(1)
