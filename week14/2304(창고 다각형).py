"""
이거 비슷한 문제를 푼 적이 있다.
왼쪽 기준으로 몇 칸 가는지 그런거 세면 되는거지 뭐. 오른쪽에서도 똑같고. 결국은 최고 봉오리가 있을 테니까.
어떤 방식으로 해도 
아 간격이 동일하지 않구나.
큰거 순으로 정렬하고, 하나씩 뽑으면서 커버를 하는거지. 커버 범위 안에 있으면 패스
만약 포함한다고 하면, 일단 자기 자신의 높이만큼은 범위에 꼭 들어간다.
그리고 또 들어가는 부분? 자기 자신의 높이 * 이전 범위까지의 차? 맞네. 쉽네
"""

N = int(input())
cols = []
start = 1001
end = 0
for _ in range(N):
    L, H = map(int, input().split())
    start = min(start, L)
    end = max(end, L)
    cols.append((L, H))
    
cols.sort(key=lambda x: x[1], reverse=True)
index = 1
i = cols[0][0]
j = cols[0][0]
area = cols[0][1]

while i > start or j < end:
    l, h = cols[index]
    if l < i:
        area += h * (i - l)
        i = l
    if l > j:
        area += h * (l - j)
        j = l
    index += 1
    
print(area)