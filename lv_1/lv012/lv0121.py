def solution(arr):
    # 제일 작은 수 제거하기
    # 리스트에서 가장 작은 값을 뺸 리스트 리턴
    # 정렬해서 리턴하라고 한적없음
    answer = []

    target = min(arr)
    arr.pop(arr.index(target))
    if arr:
        answer = arr
    else:
        answer = [-1]

    return answer

print(solution([4, 3, 2, 1]))
print(solution([10]))
