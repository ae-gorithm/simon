"""
중지 검지에 오는건 중요하지 않다.
1. 문자열에서 특정 구간에 a가 몇번 나타나는지 구하는 문제
2. l, r 포함하는 것
같은 문자열을 두고 질문을 q번 한다 -> a가 어디있는지 기억해두는게 좋을 것 같다.
S는 20자 이하. 꽤 많다.
질문의 수 q. 그리고 매번 알파벳 소문자로 구성
일단 20만이기 때문에, 매번 문자열을 다 찾는건 어려울 것 같습니다.
알파벳 몇번째 들어가는지 저장해두는게 좋을 것 같습니다.
그렇게 다 구해두고, 이분 탐색으로 위치를 찾는게 좋을 것 같습니다. l은 bisect_left로, r은 bisect_right로. 
"""
from bisect import bisect_left, bisect_right
import sys
input = lambda : sys.stdin.readline().rstrip()

# 0('a')부터 25('z')까지, 등장한 위치를 담을 리스트. 차례대로 들어가니까 당연히 정렬이 되어 있을 것
alphabets = [[] for _ in range(ord('z') - ord('a') + 1)]
string = input()
# 받은 문자열에 있는 순서대로 하나씩 집어넣기
# 복잡도 O(n) -> 200,000
for i, s in enumerate(string):
    alphabets[ord(s) - ord('a')].append(i)
    
q = int(input())
for _ in range(q):
    a, l, r = input().split()
    alphabet = alphabets[ord(a) - ord('a')]
    index_l = bisect_left(alphabet, int(l))
    index_r = bisect_right(alphabet, int(r))
    print(index_r - index_l)