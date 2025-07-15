def solution(s):
    # 문자열 내림차순으로 배치하기
    # 문자열에 s에 나타나는 문자를 큰것부터 작은순으로 정렬해서 새로운 문자열을 리턴하는 함수.
    # 대문자는 소문자보다 작은것으로 간주
    s = sorted(s, reverse=True)
    answer = ''.join(s)
    return answer


print(solution("Zbcdefg"))
