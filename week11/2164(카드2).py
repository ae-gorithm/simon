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

"""
왠지 더 쉽게 할 수 있을 것 같다.
3 7 11 15 ...
7 15 ...
15 ...
2의 제곱수만큼 그렇게 추려가야하나?
2이 제곱수가 아니면 그만큼 또 꼬이게 되니까 그게 문제네.

N이 2의 제곱일 때? -> 항상 마지막에 남는 카드가 N 그 자체!
그 외의 경우에는?
N = 10이라 생각해보자.
한바퀴 돌고나면 2 4 6 8 10
한바퀴 더 돌면 10 4 8
다음 8 4
마지막 4. 왜?

전체 카드 수 N = 2**k + r 이라고 하자.
TODO...
"""