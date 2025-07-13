"""
이렇게 풀긴 풀었는데, 그렇게 하면 시간 초과가 뜬다.
이분 탐색으로 들어갈 자리를 찾는게 나을까?
프렛의 수가 30만 이라는 점에서 문제가 생기는듯
"""
N, P = map(int, input().split())
lines = [None] + [[0] for _ in range(6)]
cnt = 0

for _ in range(N):
    line_index,  pret = map(int, input().split())
    line = lines[line_index]
    while line[-1] > pret:
        cnt += 1
        line.pop()
    if line[-1] < pret:
        cnt += 1
        line.append(pret)
print(cnt)