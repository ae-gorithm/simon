"""
개똥벌레 진짜 세네
어 이거 imoi인가 그걸로 할 수 있지 않으까
"""
N, H = map(int, input().split())
stones = [[0] * H, [0] * H]

for i in range(N):
    h = int(input())
    stone = stones[i % 2]
    stone[0] += 1
    stone[h] -= 1
    
for i in range(1, H):
    stones[0][i] += stones[0][i-1]
    stones[1][i] += stones[1][i-1]
  
cnt = 0
minimum = N
for i in range(H):
    collisions = stones[0][i] + stones[1][-(i+1)]
    if minimum == collisions:
        cnt += 1
    if minimum > collisions:
        cnt = 1
        minimum = collisions
        
print(minimum, cnt)