"""
무슨말이야 이게
그니까 이게 어떤 수가 선택이 되면, 어떤 수를 포함해서 K개만큼 뒤집히는거겠지?
오름차순으로 만들려고 한다고...? 와 이거 어떻게 푸는거지

N이 8 밑이네? 순열 경우의 수가 8!이니까 모든 경우 고려해도 되겠다.
"""
from collections import deque

N, K = map(int, input().split())
per = tuple(map(int, input().split()))
visited = set()
target = tuple(range(1, N+1))
queue = deque([(0, per)])

def flip(i):
    return per[:i] + tuple(reversed(per[i:i+K])) + per[i+K:]

while queue:
    cnt, per = queue.popleft()
    if per == target:
        print(cnt)
        break
    if per in visited:
        continue
    cnt += 1
    for i in range(0, N-K+1):
        next_per = flip(i)
        if next_per in visited:
            continue
        visited.add(per)
        queue.append((cnt, next_per))
else:
    print(-1)