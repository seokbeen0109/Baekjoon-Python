def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        slice=t[i:i+len(p)]
        if int(slice)<=int(p):
            answer+=1
    return answer