def solution(n):
    answer = 0
    for i in range(n+1):
        if i**2==n:
            answer=(i+1)**2
            return answer
        else:
            continue
    return -1