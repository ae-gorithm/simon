"""
심사관마다 시간이 다르다.
항상 이동을 해야 하는 것은 아닌게 핵심
이거 그냥 끝 시간을 기준으로 우선순위 큐이 넣어가면 되는거 아닌가? 아니 굳이 우선순위 큐가 필요한가?
N, M이 매우 큼에 유의
그냥 배수끼리 쭈욱 넣어가면 될 거 같은데
T_k와 M이 10**9 다. 즉, 복잡도가 더 생기면 안된다는 의미

아 잘못생각했다.. 심사관이 N이구나.
그럼 N에 대해서는 정렬을 해줘도 된다. 
만약 그렇게 정렬이 된 후에, 힙으로 넣고 꺼내면 안되려나? log10만인데
일단 해보자.
"""
import sys
from heapq import heappush, heappop, heapify
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
officers = [(int(input()), 1) for _ in range(N)]
heapify(officers)
for _ in range(M):
    t, n = heappop(officers)
    heappush(officers, (t // n * (n+1), n+1))
print(t)