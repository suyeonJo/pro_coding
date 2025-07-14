def solution(s):
    # 가운데 글자 가져오기
    # s의 가운데 글자를 반환하는 함수
    answer = ''

    if len(s) % 2 == 0:
        target = len(s) // 2
        answer = s[target - 1:target + 1]

    else:
        answer = s[len(s) // 2]

    return answer


print(solution("adcde"))

# def solution(s):
#     length = len(s)
#     mid = length // 2
#
#     if length % 2 == 0:
#         return s[mid - 1:mid + 1]
#     else:
#         return s[mid]