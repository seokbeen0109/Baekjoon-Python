def solution(my_string):
    answer = ''
    answer=list(my_string.lower())
    answer.sort()
    answer=''.join(answer)
    return answer