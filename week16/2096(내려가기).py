"""
메모리 4MB???
탐색을 해야하나? 근데 메모리가 4MB이다.

dp는 dp일 것 같은데, 어떻게 dp냐 -> 각 위치를 포함했을 때 얻을 수 있는 최대 점수를 구하는거지.
어쩄거나 세 개의 숫자 중 하나는 포함하는거니까.
"""

N = int(input())
max_dp = [0] * 3
min_dp = [0] * 3
index = ((0, 2), (0, 3), (1, 3))

for _ in range(N):
    v = tuple(map(int, input().split()))
    new_max_dp = []
    new_min_dp = []
    for i in range(3):
        s, e = index[i]
        new_max_dp.append(max(max_dp[s:e]) + v[i])
        new_min_dp.append(min(min_dp[s:e]) + v[i])
    max_dp, min_dp = new_max_dp, new_min_dp   
    
print(max(max_dp), min(min_dp))