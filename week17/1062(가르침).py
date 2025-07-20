"""
뭔 문제야 이게
아하... K개를 알려줄 수 있고 그것만 읽을 수 있다..
anta로 시작해서 tica로 끝난다. 그럼 일단 a, n, t, i, c는 꼭 알려줘야겠네

음 어떻게 알려주면 좋을 까. 핵심을 짚어보자. 
가장 간단하게는 모든 조합을 다 테스트하는 방법이 있는데, 너무 오래걸릴 것 같다.
단어별로 뭘 기억하고 있으면 좋을까. N은 50보다 작거나 같으니까 기억할 수 있을 것 같다.
근데 그냥 탐색하면 될 것 같은데?
한 점에서 시작해서 최대 길이가 될때까지 탐색을 하는데, 그럼 뭘 지워야 하나.
오.. 비트마스킹으로 모두 커버가 되는지 파악하는 것은 어떨까. 좀 오래걸리나?
그냥 모든 조합 다 찾아보는게 좋을 것 같은데. 다 찾아보자 그냥

1. a, n, t, i, c를 제외하고 나머지만 set으로 구현. 그리고 그걸 비트로 다 변경 -> a, n, t, i, c 뺄 필요 있나? 없다. 그냥 하자
검사를 어떻게 하지? 그냥 -?
"""
from itertools import combinations

N, K = map(int, input().split())
if K < 5:
    print(0)
    exit()
fixed = set('antatica')
    
def get_bit(word):
    return sum(1 << (ord(a) - ord('a')) for a in word) ^ sum(1 << (ord(a) - ord('a')) for a in fixed)

bits = []
alphabet = set()
for _ in range(N):
    word = set(input())
    alphabet |= word
    bits.append(get_bit(word))

remained = alphabet - fixed
comb = combinations(remained, min(K-5, len(remained)))
cnt = 0
for word in comb:
    learned_bit = get_bit(word)
    cnt = max(cnt, sum(1 if bit == bit & learned_bit else 0 for bit in bits))
    if cnt == len(bits):
        break
    
print(cnt)