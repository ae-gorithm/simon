"""
오... 주사위를 굴려가면서 이동시키는 문제
이동을 하면 바닥면이 해당 숫자로 바뀐다
그리고 그 칸의 숫자는 0으로 변경
아아 이동하면서 상단에 있는 숫자를 출력하면 되는 문제
그러면 이동시키면서 칸에 있는 값도 바꿔야 하고,
주사위의 값도 바꿔야 한다.
그럼 주사위의 참조 값은 어떻게 구현할지. 그게 문제.
주사위를 굴리는 작업을 생각해보자. 오른쪽 왼쪽으로 한다면,
상 동 하 서. 북 남은 그대로
위 아래로 굴린다면,
상 북 하 남. 동 서는 그대로.

이거를 어떻게 구현하는 것이 제일 좋을까
각 위치들에 대한 인덱스는 따로 구현해두고, 
Dice는 따로 관리하자.

정리하기
각각의 방향에 대한 값을 저장하는 Dice_value가 따로 있고,
실제로 굴러가는 아이는 dice. 이 dice에는 현재를 기준으로 어떤 value를 참조하는지에 대한 인덱스를 담고 있다.
next_index는, 그 방향으로 움직였을 때 다음 번에 이 칸에 뭐가 올지
"""

T, E, W, N, S, B = range(6)

dice_value = [0, 0, 0, 0, 0, 0]
dice = [T, E, W, N, S, B]
next_index = (None, (W, T, B, N, S, E), (E, B, T, N, S, W), (S, E, W, T, B, N), (N, E, W, B, T, S))
next_coords = (None, (0, 1), (0, -1), (-1, 0), (1, 0))

def turn(dice, dir):
    return [dice[i] for i in next_index[dir]]

def update(r, c, dice, board):
    if board[r][c] == 0:
        board[r][c] = dice_value[dice[B]]
    else:
        dice_value[dice[B]] = board[r][c]
        board[r][c] = 0
        
n, m, r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for dir in map(int, input().split()):
    nr, nc = next_coords[dir]
    if r + nr >= n or r + nr < 0 or c + nc >= m or c + nc < 0:
        continue
    r, c = r + nr, c + nc
    dice = turn(dice, dir)
    update(r, c, dice, board)
    print(dice_value[dice[T]])
    