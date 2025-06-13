"""
무슨 문제지 이게
1이 루트다.
그 다음부터 주어지는 애들은, 그냥 '연결'만 되어 있다는거지?
정렬할 필요가 있나? -> 딱히. 그러면 어떻게 관리하지? 그냥 연결그래프를 만들고, 그거부터 타고타고 들어가면 될 거 같은데.
N이 100000이니까 간단할 것 같다.
하나는 하나만 연결되어 있나? 그건 아니고

1. 이중 연결 그래프로 구현한다.
2. 1부터 연결된 노드들 꺼내가면서, 거기서부터 하나씩 토도도독
아 뭔가 방법이... 있을 것 같은데...
min을 기준으로 정렬하고.. 아 그건 아닌데

"""
from collections import deque

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

parents = [0] * (N + 1)
queue = deque([1])
while queue:
    node = queue.popleft()
    for next_node in edges[node]:
        if parents[next_node]:
            continue
        parents[next_node] = node
        queue.append(next_node)
print(*parents[2:], sep='\n')
