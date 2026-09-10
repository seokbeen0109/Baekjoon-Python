def solution(s):
    answer = ''
    s_split = s.split(' ')    # 공백 1개 기준으로만 나눠서 연속 공백도 보존
    for a in s_split:
        if a == '':             # 연속 공백으로 생긴 빈 문자열은 그대로 패스
            answer += ' '
            continue
        new = a[0].upper() + a[1:].lower()
        answer += new
        answer += ' '
    answer = answer[:-1]
    return answer