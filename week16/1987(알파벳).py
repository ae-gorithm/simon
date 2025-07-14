"""
그래프 탐색.
백트래킹
"""
import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = tuple(input() for _ in range(R))
dx = (-1, 0, 0, 1)
dy = (0, 1, -1, 0)

cnt = 0
def backtracking(r, c, trace):
    if board[r][c] in trace:
        return len(trace)
    trace.append(board[r][c])
    cnt = 0
    for x, y in zip(dx, dy):
        if 0 <= r + x < R and 0 <= c + y < C:
            cnt = max(cnt, backtracking(r+x, c+y, trace))
    trace.pop()
    return cnt

print(backtracking(0, 0, []))