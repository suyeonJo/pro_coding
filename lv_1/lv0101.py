def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    # print(answer)
    return answer

# n = int(input())
# solution(n)
