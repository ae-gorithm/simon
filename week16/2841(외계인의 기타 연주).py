"""
이렇게 풀긴 풀었는데, 그렇게 하면 시간 초과가 뜬다.
이분 탐색으로 들어갈 자리를 찾는게 나을까?
프렛의 수가 30만 이라는 점에서 문제가 생기는듯

매번 슬라이싱 하는게 문제인가?

"""

from bisect import bisect_right
import sys
input = lambda: sys.stdin.readline().rstrip()

N, P = map(int, input().split())
lines = [None] + [[0] for _ in range(6)]
cnt = 0

for _ in range(N):
    line, fret = map(int, input().split())
    pos = bisect_right(lines[line], fret)
    cnt += len(lines[line]) - pos
    lines[line] = lines[line][:pos]
    if lines[line][-1] < fret:
        cnt += 1
        lines[line].append(fret)
print(cnt)