def solution(x):
    answer = True
    x_1=str(x)
    x_2=list(x_1)
    sum=0
    for num in x_2:
        sum+=int(num)
    if x%sum==0:
        return answer
    else:
        return False