def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for x in s:
        if x.isalpha():        # 글자가 하나라도 섞여있으면
            return False        # 바로 실패 처리
    return True                 # 끝까지 다 돌았는데 글자가 없었으면 성공