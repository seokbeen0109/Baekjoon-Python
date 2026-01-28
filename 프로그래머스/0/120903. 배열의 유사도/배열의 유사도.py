def solution(s1, s2):
    count=0
    for s_1 in s1:
        for s_2 in s2:
            if s_1==s_2:
                count+=1
    answer = count
    return answer