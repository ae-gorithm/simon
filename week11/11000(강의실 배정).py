"""
이거 그리디로 안되나?
그냥 그때그때 빈 곳에 스케쥴링. 안될 것 같긴 한데.. 반례를 생각해보자.
여러 곳이 비었을 때는 어떻게 선택하지 -> 사실 어디든 상관 없을 것 같다.
그리디로 가능할 것 같다. 관건은 어떻게 정렬하고 관리하느냐

N <= 200000
S <= T <= 10 ** 9
빈 강의실이 없을 때 마다 새로운 강의실을 만드는걸로.
시간을 하나씩 지나보내야하나? -> 그럼 10**9니까 걸릴 것 같다.
스케줄링하고 하나씩 빼가면서 하자.

관리해야할 건 두 개. 
1. 우선 N개의 강의들은 시작 시간이 작은 것들부터 정렬한다.
2. 강의실 관리. 끝나는 시간을 위주로 해야한다. 강의실 번호를 관리할 필요는 없다.

어떻게 구현할까.
1. 초기 강의실 끝나는 시간은 [0] 하나만 관리한다
2. 강의를 하나씩 꺼내면서,
2-1. 가장 빨리 끝나는 강의실 시간 <= 강의 시작 시간이면 해당 강의실 시간 빼고 강의 끝나는 시간을 push
2-2. 가장 빨리 끝나는 강의실 시간 >= 강의 시작 시간이면 그냥 강의 끝나는 시간만 넣기
가보자
"""

import sys
from heapq import heappush, heappushpop

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
lectures = sorted([tuple(map(int, input().split())) for _ in range(N)])
rooms = [0]

for lec in lectures:
    s, t = lec
    first_room = rooms[0]
    if first_room <= s:
        heappushpop(rooms, t)
    else:
        heappush(rooms, t)
        
print(len(rooms))
