def solution(my_string):
    answer = 0
    for s in my_string:
        if s.isalpha():
            my_string=my_string.replace(s," ")
    my_string=my_string.split()
    for i in my_string:
        answer+=int(i)
    return answer