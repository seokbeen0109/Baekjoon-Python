def solution(numbers):
    answer = numbers[0] * numbers[1]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]*numbers[j]>answer:
                answer=numbers[i]*numbers[j]
    return answer