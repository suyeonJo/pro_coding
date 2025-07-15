def solution(price, money, count):
    # 부족한 금액 계산하기
    # 원래 이용료 price원
    # 놀이기구를 n번째 이용한다면, 원래 이용료의 n배를 받기로 한다.
    # 처음 이용료가 100이었다면, 2번쨰에는 200, 3번쨰에는 300
    # 놀이기구를 cnt번 타면 현재자신이 가지고있는 금액에서 얼마가 모자라는지 리턴
    # 넉넉하면 0 리턴
    cost = 0
    for i in range(1, count + 1):
        res = (price * i)
        cost += res

    # print(cost)
    if cost > money:
        answer = cost - money
    else:
        return 0
    return answer


print(solution(3, 20, 4))
