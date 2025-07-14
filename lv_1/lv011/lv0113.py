def solution(x):
    # 양의 정수 x가 하샤드 수
    # x의 자릿수의 합으로 x가 나누어져야한다.
    # 예를 들어 18 자릿수의 합은 9 18은 9로 나누어떨어지므로 18은 하샤드 수
    answer = True
    ori = x
    cnt = 0
    while x > 0:
        cnt += x % 10
        x = x // 10
        print(cnt)

    if ori % cnt == 0:
        # print(x)
        return answer
    else:
        return False

print(solution(11))
