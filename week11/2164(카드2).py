"""
큐를 쓰면 금방 풀릴 것 같다. N <= 500,000이니 다해봐도 될 듯
"""
from collections import deque
N = int(input())
queue = deque(range(1, N+1))

while len(queue) > 1:
  queue.popleft()
  queue.append(queue.popleft())

print(queue[0])