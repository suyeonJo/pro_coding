def solution(phone_number):
    # 핸드폰 번호 가리기
    # 폰넘버로 주어
    answer = ''
    answer = phone_number.replace(phone_number[:-4], len(phone_number[:-4]) * "*")
    # print(phone_number)
    return answer


print(solution("01033334444"))
