def solution(s):
    answer = []
    for i in range(len(s)):
        found=-1
        for j in range(i-1,-1,-1):
            if s[j]==s[i]:
                found=i-j
                break
        answer.append(found)
    return answer