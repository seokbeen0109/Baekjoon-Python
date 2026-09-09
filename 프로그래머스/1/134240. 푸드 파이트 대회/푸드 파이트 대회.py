def solution(food):
    answer = ''
    temp=''
    for i in range(1,len(food)):
        if food[i]%2!=0:
            food[i]=food[i]-1
        for j in range(food[i]//2):
            temp+=str(i)
    answer+=temp
    answer+='0'
    answer+=temp[::-1]
    return answer