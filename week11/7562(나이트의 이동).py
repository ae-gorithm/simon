"""
칸은 300 * 300까지
모든 경우의 수 다 구할 수 있을 것 같은데
너비 우선 탐색으로 하면서 count를 세면 될 것 같다.
테스트 케이스 수가 얼마인지 모르니까 전부 탐색하기가 좀 그러네.
이동 가능한 방향을 계산해야하나?
최대한 가까이 간 후에 거기서부터 탐색을 하는건가. 일단은 그 방향으로 계속 가는게 맞나...
"""

from collections import deque
# 시계방향
dx = (1, 2, 2, 1, -1, -2, -2, -1)
dy = (-2, -1, 1, 2, 2, 1, -1, -2)

def get_next_step(i, j, c, board):
    l = len(board)
    return tuple((i + x, j + y, c) for x, y in zip(dx, dy) if 0 <= i + x < l and 0 <= j + y < l and board[i+x][j+y] > c)

T = int(input())
cnts = []
for _ in range(T):
    l = int(input())
    MAX = l ** 2
    board = [[MAX] * l for _ in range(l)]
    si, sj = map(int, input().split())
    di, dj = map(int, input().split())
    queue = deque([(si, sj, 0)])
    while queue:
        i, j, c = queue.popleft()
        if board[i][j] <= c:
            continue
        board[i][j] = c
        if i == di and j == dj:
            break
        next_step = get_next_step(i, j, c+1, board)
        queue.extend(next_step)
    cnts.append(str(c))
    
print(*cnts, sep='\n')