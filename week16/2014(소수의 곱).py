"""
하나를 뺄 때마다 하나를 더하는게 나을 것 같은데.
그래프로 들어가면 끝도 없을 것 같고,
음.. 튜플을 다 저장해놓는 식으로 다시 가볼까? -> 아니다
소수가 핵심일 것 같은데... 음 그렇다고 매번 다 추가하기도 그렇고.
정답이 2**31보다 작은 자연수라는 것도 뭔가 있다.
오름차순으로 주어진다!
하나씩 다 곱하면서, max보다 큰거까지만 넣을까?

그냥 다 넣는다고 생각해보자.

메모리 초과 이유 -> 하나당 100개가 더 추가된다.
일단 지금 하는대로 하고, pop을 해보자. 그럼 heap을 쓰면 안될 것 같은데.

애초에 중복되지 않는것만 넣을 수 없나?

"""
from heapq import heappush, heappop
    
MAX = 2 ** 31
K, N = map(int, input().split())
primes = tuple(map(int, input().split()))

heap = [1]

for _ in range(N):
    item = heappop(heap)
    for p in primes:
        val = item*p
        if val >= MAX:
            continue
        heappush(heap, val)
        if item % p == 0:
            break

print(heap[0])