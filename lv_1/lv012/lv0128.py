def solution(s):
    # 문자열 다루기 기본
    # 문자열 s의 길이가 4 혹은 6
    # 숫자로만 구성된건지 확인해주는 함수
    # s a234 false  1234면 true

    answer = True
    for x in s:
        if not x.isdecimal():
            return False
    else:
        if len(s) == 4 or len(s) == 6:
            return answer
        else:
            return False





print(solution("a234"))
