def solution(s):
    answer = True
    if s[0]==")" or s[-1]=="(":
        answer=False
    else:
        c1=0 # (개수
        for i in range(len(s)):
            if s[i]=="(":
                c1+=1
            else:
                c1-=1
            if c1<0:
                answer=False
        if c1>0:
            answer=False
    return answer