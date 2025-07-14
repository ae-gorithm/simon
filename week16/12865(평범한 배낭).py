"""
자주 풀었던거
dpdp

1. dp에 담겨있는 값은, 현재까지의 물품들을 넣었을 때 이 무게에서 얻을 수 있는 최대 가지

불쌍한 준서 잘다녀와라
"""
import sys
N, K = map(int, input().split())
input = lambda : sys.stdin.readline().rstrip()

dp = [0] * (K + 1)

for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K-w, -1, -1):
        dp[i + w] = max(dp[i + w], dp[i] + v)

print(dp[-1])