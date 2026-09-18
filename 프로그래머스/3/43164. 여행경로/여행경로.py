def solution(tickets):
    answer = []
    route ={}
    for a, b in tickets:
        if a not in route:
            route[a]=[]
        route[a].append(b)
        
    for airport in route:
        route[airport].sort()
    
    n=len(tickets)

    def dfs(current, path):
        if len(path)==n+1:
            answer.append(path[:])
            return True
        if current not in route:
            return False
        for i in range(len(route[current])):
            next_airport=route[current][i]
            if next_airport is None:
                continue
            route[current][i]=None
            path.append(next_airport)
            if dfs(next_airport, path):
                return True
            path.pop()
            route[current][i]=next_airport
        return False
    
    dfs("ICN", ["ICN"])
    return answer[0]