def solution(numbers):
    # 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers
    # 찾을수 없는 numbers 0~ 9 까지의 숫자를 모두 찾아 더한 수
    answer = 0

    for i in range(10):  # 상수반복 10번
        if i not in numbers:  # 리스트 값만큼 반복 n
            answer += i

            # O(10*n)
    
    # print(answer)

    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
