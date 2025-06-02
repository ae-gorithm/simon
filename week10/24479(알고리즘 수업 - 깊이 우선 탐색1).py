"""
기본 깊이 우선 탐색 문제
"""
N, M, R = map(int, input().split())
graph = [None] + [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for edges in graph[1:]:
    edges.sort(reverse=True)

visited = dict([(i, 0) for i in range(1, N+1)])
order = 1
stack = [R]
while stack:
    curr_node = stack.pop()
    if visited[curr_node]:
        continue
    visited[curr_node] = order
    order += 1
    
    for next_node in graph[curr_node]:
        if visited[next_node] == 0:
            stack.append(next_node)
            
print(*visited.values(), sep='\n')