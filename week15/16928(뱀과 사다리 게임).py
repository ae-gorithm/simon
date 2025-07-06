"""
오잉 일단 주사위를 굴린 겨로가가 100번 칸을 넘어간다면 이동할 수 없다!!
이거 그래프 같은데. 최단 경로 찾기
다익스트라로 가보자
그래프로 어떻게 연결할 것인가가 관건
주사위 굴려서 갈 수 있는 거리라면 웨이트 1
뱀이 나오는 곳이라면 안가는게 낫나? 동시에 나오는 경우가 없으니까, 피할 수 있다면 무조건 피하는게 맞겠지. 그 간선은 빼는걸로.
"""
from heapq import heappush, heappop

N, M = map(int, input().split())
graph = [[]] + [[(i+j, 1) for j in range(1, min(100-i+1, 7))] for i in range(1, 100)]
for _ in range(N + M):
    x, y = map(int, input().split())
    graph[x] = [(y, 0)]
        
heap = [(0, -1)]
distance = [float('inf')] * 101

while heap:
    dist, node = heappop(heap)
    node *= -1
    if distance[node] < dist:
        continue
    distance[node] = dist
    if node == 100:
        break
    for n, w in graph[node]:
        if distance[n] > dist + w:
            heappush(heap, (dist + w, -n))
            
print(distance[100])