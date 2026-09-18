from functools import lru_cache

def solution(numbers, target):
    n=len(numbers)
    
    @lru_cache(maxsize=None)
    def dfs(index,total):
        if index==n:
            return 1 if total==target else 0
        
        return dfs(index+1, total+numbers[index]) + dfs(index+1, total-numbers[index])
    return dfs(0,0)