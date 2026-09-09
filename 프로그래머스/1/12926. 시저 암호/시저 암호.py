def solution(s, n):
    answer = ''
    
    for ch in s:
        if ch.isupper():                          # 대문자인 경우
            answer += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        elif ch.islower():                        # 소문자인 경우
            answer += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        else:                                      # 알파벳이 아닌 경우 (공백 등)
            answer += ch
    
    return answer