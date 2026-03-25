# https://www.acmicpc.net/problem/11724

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘리기
n, m = map(int, input().split()) # 정점, 간선의 개수
count =0 # dfs 수행 횟수
visited=[False]*(n+1)
def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        count+=1
        
print(count)

