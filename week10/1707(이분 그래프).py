"""
이분그래프의 정의
각 집합에 속한 정점끼리는 서로 인접하지 않는다.
다른 집합에서는 상관 없다.

여기서 방향은 중요하지 않은 것 같다. 한방향으로라도 이어져 있으면 '인접'하다고 본다.

가정을 해보자.
이분 그래프로 나뉠 수 있다면, 하나의 정점이 분명 어느 하나의 집합에는 들어가게 될 것이다.
그렇다면, 임의의 점을 잡고, 그 점과 연결되지 않은 모든 정점들을 다 모아서 하나의 집합으로 만들었을 때
그 나머지 점들이 전부 각각 연결되지 않았다면 이분 그래프로 나뉠 수 있는 것.
이게 모든 경우를 찾을 수 있나? -> O

그러나 이 경우는 임의의 점 외의 다른 점들도 서로 이어져 있지 않다는 것을 보장해주지 않는다.

그럼 다른 방식으로 구해야한다.
나는 연결 그래프를 찾을 수 있다. 이건 반대로 전혀 연결되지 않는 그래프를 찾는 것.
그럼 탐색을 하는데, 연결되지 않은 노드들을 다 탐방해보는건? -> 그렇게 단순하진 않다.

한 점에서 깊이 우선 탐색을 한다고 생각해보자. 그러면 서로 번갈아가면서 집합에 넣어야 한다.
그렇다면, 1. 점을 탐색할 때 홀수번째인지 짝수번째 인지를 같이 기록하면서 탐색한다. 2. 기록된 순서를 바탕으로 집합에 넣되, 집합에 있는 노드 중 연결된 노드가 있으면 Fail이다.

이 방식이 반드시 이분 그래프를 판별할 수 있다고 할 수 있나?
과연 임의의 점에서 깊이 우선 탐색을 한다해도 반드시 보장할 수 있나? -> O! 어떻게든 그 일부분의 그래프는 넣어야하기 때문에.
그럼 구현해보자.
set으로 구현하는 것이 맞나?
나랑 인접한 점도 set으로 구현하는 것이 맞으려나? -> 둘 중 하나만 set이면 될 것 같다.
만약 깊이 우선 탐색을 할 때까지는 이분 그래프가 맞았는데 끊긴다면? 즉 모든 노드가 탐색된 것이 아니라면?
안 탐색된 것을 바탕으로 다시 넣어야 할 것 같다. 아무랑도 연결되어 있지 않으니 어차피 아무데나 넣어도 상관 없을듯
"""

K = int(input())
answers = []
           
def dfs(start, visited, edges, count = 0):
    stack = [(1, start)]
    while stack:
        order, curr_node = stack.pop()
        if visited[curr_node]:
            continue
        edge = edges[curr_node]
        if any(visited[next_node] == order for next_node in edge):
            return 'NO', count
        visited[curr_node] = order
        order *= -1
        count += 1
        for next_node in edge:
            if visited[next_node] == 0:
                stack.append((order, next_node))
    return 'YES', count
    
for _ in range(K):
    V, E = map(int, input().split())
    edges = [None] + [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
        
    visited = [None] + [0] * (V)
    count = 0
    answer = 'YES'
    while count < V:
        start = visited.index(0)
        answer, count = dfs(start, visited, edges, count)
        if answer == 'NO': break
    answers.append(answer)
    
print(*answers, sep='\n')