"""
이거 그거 같은데, 가방안에 넣는거.
각 체력마다 얻을 수 있는 max를 찾아 가는거지.
"""

N = int(input())
L = tuple(map(int, input().split()))
J = tuple(map(int, input().split()))
happiness = [0] * 101

for i in range(N):
    l, joy = L[i], J[i]
    for j in range(100, l, -1):
        happiness[j] = max(happiness[j], happiness[j-l] + joy)

print(max(happiness))