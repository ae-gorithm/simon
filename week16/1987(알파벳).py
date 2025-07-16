"""
이진으로 풀되, visited에 해당 칸에 해당 비트로 들어왔을 때의 최댓 값을 넣는거지
"""
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = tuple(tuple(map(lambda x: 2 ** (ord(x)-65), input())) for _ in range(R))
dx = (-1, 0, 0, 1)
dy = (0, 1, -1, 0)
visited = [[defaultdict(lambda: -1) for _ in range(C)] for _ in range(R)]

# bit은 board[r][c] 포함 X
def backtracking(r, c, bit=0, visited=visited):
    # 만약 방문한 곳이라면?
    if visited[r][c][bit] < 0:
        if board[r][c] & bit:
            visited[r][c][bit] = 0
        else:
            visited[r][c][bit] = 1
            next_step = [(r+x, c+y) for x, y in zip(dx, dy) if 0 <= r+x < R and 0 <= c+y < C]
            new_bit = bit | board[r][c]
            for nr, nc in next_step:
                visited[r][c][bit] = max(visited[r][c][bit], 1 + backtracking(nr, nc, new_bit))
    return visited[r][c][bit]

print(backtracking(0, 0))