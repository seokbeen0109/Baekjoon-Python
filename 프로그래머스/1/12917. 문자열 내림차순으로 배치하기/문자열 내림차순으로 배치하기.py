def solution(s):
    answer = ''
    s_1=list(s)
    s_1.sort()
    s_1.reverse()
    for alpha in s_1:
        answer+=alpha
    return answer