"""
그리디 일 것 같긴 하다.
그렇다고 마냥 가장 높은 것들을 듣기에는 마감일까지 남은 일수가 있다.
뒤에서 부터 배치하면 되지 않나?
가장 높은걸 끝낼 수 있는 마지막날 해버리면? 그럼 앞에 꺼도 다 할 수 있지 않을까? 그럼 다 할 수 있나?
어떻게 보장하지?
만약 작은 것을 넣으려고 하는데, 넣을 수 있는 자리가 없어. 그러면 사실 더 높은 것들이 다 들어갔다고 보면 되는거고
그 앞에 더 작은게 있다? 그럴 수는 없다. 
만약 같은 점수라면? 큰거부터 넣는게 낫지
"""
from heapq import heappush, heappop

N = int(input())

heap = []
lastday = 0
for _ in range(N):
    d, w = map(lambda x: -int(x), input().split())
    heappush(heap, (w, d))
    lastday = min(lastday, d)

score = 0
avail = [True] * (-lastday + 1)

while heap:
    w, d = map(lambda x: -x, heappop(heap))
    for day in range(d, 0, -1):
        if not avail[day]: continue
        avail[day] = False
        score += w
        break
    
print(score)