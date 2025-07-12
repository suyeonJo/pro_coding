def solution(s):
    # 대문자와 소문자가 섞인 문자열 s
    # 대문자 소문자 구분없이 갯수 비교

    s = s.upper()
    # print(s)
    a = 0
    b = 0
    for x in s:
        if x == "P":
            a += 1
        elif x == "Y":
            b += 1

    if a == b:
        answer = True
    else:
        answer = False

    return answer


print(solution("ppewqyy"))
