def solution(s):
    answer = ''
    word=s.split(' ')
    for a in word:
        for i in range(len(a)):
            if i%2==0:
                answer+=a[i].upper()
            else:
                answer+=a[i].lower()
        answer+=" "
    answer=answer[:-1]
    return answer