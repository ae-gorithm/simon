"""
일단 부하 문화에서 트리가 생각나구요
이것도 왠지 imoi으로 구할 수 있지 않을까?
그냥 칭찬 받은 정도 다 저장해놓고, 자기 상사가 칭찬받으면 다 칭찬을 받는거잖아?
그럼 상사에서부터 타고 오면서 업데이트 해주면 되겠다.
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
seniors = [0] + list(map(int, input().split()))
praises = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    praises[i] += w

for i in range(2, n+1):
    senior = seniors[i]
    praises[i] += praises[senior]
    
print(*praises[1:])