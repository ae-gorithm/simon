"""
set이 아니라 비트마스킹으로 해보자.
그리고 어떤 지점을 탐색했는지를 파악ㅇ르 해두자.
"""
import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = tuple(tuple(map(lambda x: 2 ** (ord(x)-65), input())) for _ in range(R))
dx = (-1, 0, 0, 1)
dy = (0, 1, -1, 0)

def backtracking(r, c, bit=0, cnt=0):
    if board[r][c] & bit:
        return cnt
    bit |= board[r][c]
    cnt += 1
    next_step = [(r+x, c+y) for x, y in zip(dx, dy) if 0 <= r+x < R and 0 <= c+y < C]
    for nr, nc in next_step:
        new_cnt = max(cnt, backtracking(nr, nc, bit, cnt))
    return new_cnt

print(backtracking(0, 0))