def solution(arr1, arr2):
    # 행렬의 덧셈
    # 행렬의 덧셈은 행과 열의 크기가 같은 두행렬의 같은행, 같은 열의 값을 서로 더한 결과
    # 2차원 배열
    answer = []
    for i in range(len(arr1)): #행
        tmp = []
        for j in range(len(arr1[0])): #열
            vals = arr1[i][j] + arr2[i][j]
            tmp.append(vals)
        answer.append(tmp)

    # print(answer)

    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
