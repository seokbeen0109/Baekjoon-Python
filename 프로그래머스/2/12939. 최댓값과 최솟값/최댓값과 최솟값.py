def solution(s):
    answer = ''
    s_split=s.split()
    nums=list(map(int, s_split))
    answer+=str(min(nums))
    answer+=" "
    answer+=str(max(nums))
    return answer