def solution(strings, n):    
    def get_char(s):
        return s[n] 
    strings.sort()             
    strings.sort(key=get_char)
    return strings