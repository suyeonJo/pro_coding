def solution(seoul):
    # 서울에서 김서방 찾기
    # 리스트에서 김씨의 인덱스 위치를 찾아 리턴하기
    # answer = ''
    res = seoul.index("Kim")
    # print(res)
    answer = f'김서방은 {res}에 있다'

    return answer


print(solution(["Jane", "Kim"]))
