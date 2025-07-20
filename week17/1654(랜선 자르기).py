"""
이미 자른 랜선은 다시 붙일 수 없다. %가 적당할듯
이것도 이분 탐색인가?
K가 1 이상 10,000 이하.
N이 1,000,000 이하의 정수. N개를 만들고 싶어한다. 

%와 sum을 이용할 것 같긴 하다. 그럼 어떻게?
N개를 만들 수 있는 랜선의 최대 길이! 가장 긴걸로 하면 하나밖에 안만들어질 것 같다.
길이를 줄일수록 N은 늘어난다.

일단 이분 탐색으로 하자.
만약 N이 같을때도 포함
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def get_sum(length, LAN):
    return sum(l // length for l in LAN)

K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]
length = max(LAN) * 2
start, end = 1, length
while start <= end:
    mid = (start + end) // 2
    sum_length = get_sum(mid, LAN)
    if sum_length >= N:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)