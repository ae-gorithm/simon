"""
이걸 DP로 구한다면?
어디에서 들어오는지만 중요한게 아니라 그냥 다 중요하니까. 이걸 뭐... -> 안될 것 같다.
백트래킹인데, 반복문으로 풀어보자.
"""
import sys
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = tuple(input() for _ in range(R))
dx = (-1, 0, 0, 1)
dy = (0, 1, -1, 0)
stack = [(0, 0, set())]

cnt = 0

# 반복문에서는 Trace 문제를 어떻게 해결할까.
# stack마다 set을 저장해두긴 좀 그렇고. 그럴건뭐야
while stack:
    r, c, trace = stack.pop()
    if board[r][c] in trace:
        cnt = max(cnt, len(trace))
        continue
    trace.add(board[r][c])
    next_step = [(r+x, c+y) for x, y in zip(dx, dy) if 0 <= r + x < R and 0 <= c + y < C and board[r+x][c+y] not in trace]
    if len(next_step) == 0:
        cnt = max(cnt, len(trace))
    for nr, nc in next_step:
        stack.append((nr, nc, set(trace)))
            
print(cnt)