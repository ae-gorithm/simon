"""
가장 가까운 소수 좌우로 구하면 되네
소수 구하기 알고리즘 있었는데 뭐였더라
모든 소수 저장하고 있어도 될 것 같은데
테스트 케이스가 여러개다 보니, 처음에 그냥 다 구해놓고 해도 될 것 같기도 하고.
아니면 테스트케이스 지날때마다 기억하고 있어야지.
에라토스테네스의 체로 구하되, 기억을 하고 있는게 낫겠다.
아니 그럴거면 그냥 처음부터 1299709까지의 소수 다 구하고 포함시키면 안되나? 너무 복잡도가 커질 것 같다
일단 해보자
"""
from math import sqrt

def is_prime(k):
    if k % 2 == 0:
        return False
    for i in range(3, int(sqrt(k)) + 1, 2):
        if k % i == 0:
            return False
    return True

T = int(input())
maximum = 0
K = []

for _ in range(T):
    k = int(input())
    maximum = max(maximum, k)
    K.append(k)

prime = [True] * (maximum + 1)
prime[0:2] = [False] * 2

for i in range(2, int(sqrt(maximum))+1):
    if prime[i]: 
        for j in range(i ** 2, maximum+1, i):
            prime[j] = False

while prime[-1] == False:
    i = len(prime)
    prime.append(is_prime(i))
    

results = []
for k in K:
    if prime[k]:
        result = 0
    else:
        left = prime[k:k//2:-1].index(True)
        right = prime[k:].index(True)
        result = left + right
    results.append(result)

print(*results, sep='\n')
# 매번 찾는게 효율적일듯