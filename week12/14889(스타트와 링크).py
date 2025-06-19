"""
... 팀을 반반 나눠야 한다는걸 이제 알았네
그냥 조합으로 하자...
"""

from itertools import combinations

def team_to_bin(team):
    return sum(2 ** i for i in team)

N = int(input())
board = tuple(tuple(map(int, input().split())) for _ in range(N))
teams = list(combinations(range(N), N // 2))
stats = dict()

minimum = 100 * N * N
everyone = 2 ** N - 1

for team in teams:
    stat = sum(board[i][j] for j in team for i in team)
    stats[team_to_bin(team)] = stat

for team in teams:
    binary = team_to_bin(team)
    minimum = min(minimum, abs(stats[binary] - stats[everyone ^ binary]))
    
print(minimum)