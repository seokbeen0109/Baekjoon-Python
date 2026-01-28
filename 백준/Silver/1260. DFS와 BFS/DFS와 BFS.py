# https://www.acmicpc.net/problem/1260
from collections import deque
n, m, v = list(map(int, input().split()))

def dfs(graph,v,visited):
    visited[v]=True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, v, visited):
    queue=deque([v])
    visited[v]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1): # 번호가 낮은 노드부터 방문하도록 sort
    graph[i].sort()

visited_dfs=[False]*(n+1)
visited_bfs=[False]*(n+1)

dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)
