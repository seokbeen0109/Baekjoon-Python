def solution(my_string):
    answer = ''
    for string in my_string:
        if string.isupper()==True:
            answer+=string.lower()
        else:
            answer+=string.upper()
    return answer