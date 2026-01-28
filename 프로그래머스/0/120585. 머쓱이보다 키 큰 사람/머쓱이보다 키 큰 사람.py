def solution(array, height):
    count=0
    array.sort()
    for h in array:
        if h>height:
            count+=1
    answer = count
    return answer