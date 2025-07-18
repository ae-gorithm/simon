"""
시간 제한이 0.5이다.
버스의 개수는 100,000개나 된다.
이걸 루프를 돌면서 다 처리할 수 있나...?
다익스트라 같은데, 제일 간단한 방법부터 가보자.
"""

import sys
from heapq import *
input = lambda : sys.stdin.readline().rstrip()
INF = 10 ** 8

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))

F, T = map(int, input().split())
if F == T:
    print(0)
    exit()
dists = [INF] * (N + 1)
heap = list(graph[F])
heapify(heap)

"""
원리를 잘 생각해보자.
한 점에서 시작해서, 이을 수 있는 거리들을 최단거리 순으로 업데이트하면, 제일 작은것 부터 포함되는 것이 보장이 된다 당연히. 그럼 distance 그 자체를 배열로 두는게 낫지 않을까?
그 후에 들어오는 친구들이 더 작을수도 있긴 하지. 근데 그럼 관리가 되냐는게 문제.
"""
while heap:
    d, e = heappop(heap)
    if dists[e] <= d:
        continue
    dists[e] = d
    if e == T:
        break
    for nd, ne in graph[e]:
        if dists[ne] > d + nd:
            heappush(heap, (d + nd, ne))
            
print(dists[e])