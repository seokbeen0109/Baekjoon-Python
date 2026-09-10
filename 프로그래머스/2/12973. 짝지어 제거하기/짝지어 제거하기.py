def solution(s):
    stack = []
    
    for ch in s:
        if stack and stack[-1] == ch:   # 스택 맨 위와 지금 글자가 같으면
            stack.pop()                    # 짝이 맞았으니 제거
        else:
            stack.append(ch)               # 다르면 쌓기
    
    return 1 if not stack else 0    # 다 제거됐으면(스택이 비었으면) 1, 아니면 0