"""
곱과 합의 차가 가장 적은 것을 찾는다. 만약 모든 경우의 수를 고려한다면 시간 복잡도는?
10, 10*9 / 2, 10*9*8 / 6, ..., 10 이런식인데
가장 높은 값인 10*9*8*7*6/5*4*3*2*1 해봤자 사실 얼마 안된다.
그냥 모든 경우의 수를 구하는 것으로 가보자. 
"""
from itertools import combinations

N = int(input())
tastes = tuple(tuple(map(int, input().split())) for _ in range(N))
total_taste = 10**9

for i in range(1, N+1):
    comb = combinations(tastes, i)
    for taste_comb in comb:
        sour, bitter = 1, 0
        for taste in taste_comb:
            sour *= taste[0]
            bitter += taste[1]
        total_taste = min(total_taste, abs(sour - bitter))
        if total_taste <= 1:
            break
    
print(total_taste)