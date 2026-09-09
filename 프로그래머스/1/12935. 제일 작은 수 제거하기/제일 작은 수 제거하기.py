def solution(arr):
    answer = []
    if len(arr)==1:
        answer.append(-1)
        return answer
    else:
        arr.remove(min(arr))
        for num in arr:
            answer.append(num)
        return answer