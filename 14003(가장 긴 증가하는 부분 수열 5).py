"""
LIS 알고리즘이다.
근데 마지막에 실제 값도 구현을 하긴 해야한다. 이건 어떻게 하지?
각 요소들이 몇번째 들어갔는지 기억하고 있다가
마지막부터 쭈루루루 내려오면 되겠다!
"""
from bisect import bisect_left as index

N = int(input())
seq = tuple(map(int, input().split()))
pos = []
dp = []

for e in seq:
    i = index(dp, e)
    if i == len(dp):
        dp.append(e)
    else:
        dp[i] = e
    pos.append(i)

LIS = []
i = len(dp) - 1

for j, p in enumerate(reversed(pos)):
    j = N - 1 - j
    if p == i:
        LIS.append(seq[j])
        i -= 1

print(len(LIS), ' '.join(map(str, reversed(LIS))), sep='\n')