def solution(s):
    n = len(s)
    answer = 0
    pairs = {')': '(', ']': '[', '}': '{'}   # 닫는 괄호: 그 짝이 되는 여는 괄호
    
    for x in range(n):
        rotated = s[x:] + s[:x]     # 왼쪽으로 x칸 회전
        
        stack = []
        valid = True
        for ch in rotated:
            if ch in '([{':           # 여는 괄호면 쌓기
                stack.append(ch)
            else:                      # 닫는 괄호면
                if not stack or stack[-1] != pairs[ch]:  # 짝이 안 맞으면
                    valid = False
                    break
                stack.pop()             # 짝 맞으면 제거
        
        if valid and not stack:   # 끝까지 무사했고, 남은 괄호도 없으면
            answer += 1
    
    return answer