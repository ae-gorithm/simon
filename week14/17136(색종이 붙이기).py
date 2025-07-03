"""
단순히 가장 큰거부터 갖다 붙인다고 풀리는건 아닌 것 같다.
할 수 있는 모든 경우의 수를 찾아야 할 듯
가장 큰거부터 갖다 대면서 풀고, 푸는 방법 없으면 되돌아가고 이런식
푸는 방법 있으면 기억해뒀다가, 그 다음 풀이방법에서 최소를 구하는거지

핵심
1. 이 종이를 넣어도 되는 공간을 어떻게 찾지?
2. 종이를 붙였다고 치고, 새로운 공간은 어떻게 전달하지?

방안
일단 '어떤' 방식으로 정리하고,
그렇게 정리된 것에서 5, 4, 3, 2, 1 크기의 1들을 찾는게 좋을 듯
'어떤' 방식으로 정리하는게 좋을까? -> 2차원 배열이 가장 직관적인 것 같다.
종이의 크기가 100이다. 그리고 각 종류의 색종이는 5개씩이니까, 총 25개. 붙였다 뗐다 할 수 있는 경우의 수는 최악의 경우에도 2 ** 17. 충분히 고려할 수 있겠다.

자 이제 백트래킹을 어떻게 할 것인지가 중요하다.
1. 1로 시작하는 공간을 찾는다.
2. 해당 공간을 Queue에 넣어야 한다. -> 왜? 굳이 그럴 필요는 없을 것 같다.
2-1. 어쨌든 1로 시작하는 공간을 찾았으면 색종이를 붙여야 사라지니까.
3. 남은 종이의 수에 따라, 붙일 수 있는 5, 4, 3, 2, 1를 붙인 경우의 수 중 가장 작은걸 택한다.

그럼 dfs에서 반환해야 할 것 및 종료 조건
1. 더이상 붙일 색종이가 없으면 -1
2. 붙일 색종이는 있는데 can_detach가 모두 안되면 -1
3. 만약 다 붙였으면 cnt 반환
4. cnt들 중에서 가장 작은걸 최종 경우의 수로 하면 되는데, -1은 제외 
"""

board = [list(map(int, input().split())) for _ in range(10)]

def can_attach(r, c, l):
    if r + l > 10 or c + l > 10:
        return False
    for i in range(r, r+l):
        for j in range(c, c+l):
            if board[i][j] == 0:
                return False
    return True

def update(r, c, l, detach=False):
    value = 1 if detach else 0
    for i in range(r, r+l):
        for j in range(c, c+l):
            board[i][j] = value

def find_next():
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                return i, j
    return -1, -1

papers = [5, 5, 5, 5, 5]

def dfs():
    r, c = find_next()
    cnt = 25 - sum(papers)
    if r == -1 and c == -1:
        return cnt
    if cnt == 25:
        return -1
    min_result = float('inf')
    for i in range(4, -1, -1):
        if papers[i] == 0:
            continue        
        l = i + 1
        if not can_attach(r, c, l):
            continue
        update(r, c, l)
        papers[i] -= 1
        result = dfs()
        if result >= 0:
            min_result = min(min_result, result)
        update(r, c, l, True)
        papers[i] += 1
        
    return min_result if min_result != float('inf') else -1

print(dfs())