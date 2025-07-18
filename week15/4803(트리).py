"""
완전 연결 그래프도 가능하네.
처음에 연결 요소는 왜 언급 한거지?
트리가 있냐 없냐를 판단하는 것이 아니라 전체 트리의 개수를 찾는거다.

n이 500이다 => n**3도 가능하다.
문제를 잘 이해를 못하겠다.
사이클이 있을 때, 빼버린다면? 그건 해당 안하는 거겠지.

예제를 보고 파악하자.
1. 점 하나만 있어도 트리라고 본다.
2. 간선을 빼고 파악하는건 안된다.
대충 알겠다.

순회를 돌긴 할텐데, 순회를 돌다가 사이클이 생기면, 해당 사이클 내의 점들은 다 제거해버릴까?
포함이 안되는 거지. 사이클이 있고, 그 사이클과 연결된 점들은 전부 탈락인거잖아.
결국 한 점에서 탐색을 하다가, 같은 점이 나온다면 그 탐색의 결과로 나온 점들은 전부 트리가 아니게 된다. 탐색 결과 사이클이 없어야 트리인거다. 너비우선이든 깊이우선이든.
ㅇㅋ 그렇게 가보자. 그럼 관리는? Set으로 하는걸로. Set 2개를 둘 필요는 없겠지? 그냥 하나 두고 돌면서 넣자.
순회마다 Set을 돌고, 또 전체 Set을 둬야할 것 같다. 그래서 그 Set에 없는 것 위주로
"""
from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

case = 1
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    tree_cnt = 0
    remained = set(e for e in range(1, N+1))

    while remained:
        e = remained.pop()
        visited = set()
        q = deque([(e, 0)])
        is_cycle = False
        
        while q:
            c, p = q.popleft()
            if c in visited:
                is_cycle = True
                continue
            visited.add(c) 
            for n in graph[c]:
                if n != p:
                    q.append((n, c))
        
        remained -= visited
        tree_cnt += 0 if is_cycle else 1
        
    result = f"Case {case}: " + ("No trees." if tree_cnt == 0 else "There is one tree." if tree_cnt == 1 else f"A forest of {tree_cnt} trees.")
    print(result)
    case += 1