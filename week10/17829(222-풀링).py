N = int(input())
board = list(list(map(int, input().split())) for _ in range(N))
STRIDE = 2
"""
STRIDE를 기준으로 행과 열을 뛰어가면서 계산하면 될 것 같다.
매번 작업할 때마다 새로운 리스트를 생성해서 할당해주면 되고.
근데 다른 방법이 있을 것 같다.
2번째로 작은 수 끼리 해서 그 중에서 또 2번째로 작은 수. 뭔가 
"""

def convolution(board, STRIDE):
    n = len(board)
    if n == 1:
        return board
    
    new_board = [[0] * (n // STRIDE) for _ in range(n // STRIDE)]
    
    for i in range(0, n, STRIDE):
        for j in range(0, n, STRIDE):
            value = sorted(board[i][j:j+STRIDE] + board[i+1][j:j+STRIDE])[2]
            new_board[i//STRIDE][j//STRIDE] = value
            
    return convolution(new_board, STRIDE)

print(convolution(board, STRIDE)[0][0])