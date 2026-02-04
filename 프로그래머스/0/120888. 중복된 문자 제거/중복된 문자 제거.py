def solution(my_string):
    answer = ''
    count=[]
    for s in my_string:
        if s not in count:
            count.append(s)
            answer+=s
    return answer