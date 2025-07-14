def solution(absolutes, signs):
    # 절대값을 차례대로 담은 정수배열, 정수들의 부호를 차례대로 담은 불린 배열
    # 각 배열의합을 구하기
    answer =0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    # print(answer)
    return answer


print(solution([4, 7, 12],[True,False,True]))
