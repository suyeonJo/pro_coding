def nums(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    return cnt

# 맞습니다! 컴프리헨션보다는 명확한 for 루프가 더 읽기 쉽고 이해하기 좋네요.
# 코드를 보니 약수의 개수를 구하는 함수와 메인 로직이 잘 분리되어 있어서 구조가 깔끔합니다.
# 한 가지 성능 개선 팁을 드리자면, nums 함수에서 약수를 구할 때 sqrt(x)까지만 반복해도 됩니다:

def solution(left, right):
    # 약수의 개수와 덧셋
    # 두 정수 left 와 right 가 매개변수로 주어짐
    # 왼쪽에서 오른쪽까지 모든 수들 중 약수의 개수가 짝수인것 더함
    # 홀수인것 뺌
    answer = 0

    for i in range(left, right + 1):
        if nums(i) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


print(solution(13, 17))
