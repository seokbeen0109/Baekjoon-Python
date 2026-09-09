def solution(s):
    answer = True
    p_count=0
    y_count=0
    s=s.lower()
    s_1=list(s)
    for a in s:
        if a=='p':
            p_count+=1
        elif a=='y':
            y_count+=1
    if p_count==y_count:
        return True
    else:
        return False