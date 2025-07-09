"""
dp!
이미 방문한 도시들을 비트마스킹으로 처리하고, -> visited
마지막으로 방문한 도시를 last라고 하자.
그럼 dp[visited][last]를 구할 수 있다.
거기에는 뭐가 들어가려나? visited를 모두 방문하는데, 마지막 점이 last인 최단 경로
근데 결국 갔다가 오려면, 시작점이 어딘지 알아야하는거 아닌가? -> 시작 점도 기억하고 있어야 한다. -> 굳이? 어차피 최단 경로가 정해진다면 0에서 출발해서 0으로 돌아오는 길이 있을 거고 그렇게 해서 구해질텐데?
방문하는 도시를 늘려가면서 dp를 업데이트
업데이트는 어떻게? 마지막 점과 새로 방문하는 점을 잇는 거리를 추가하면 됨
"""
from itertools import combinations

N = int(input())
maximum_cost = 10 ** 6 + 1
costs = tuple(tuple(map(int, input().split())) for _ in range(N))
# dp[i][j] = v -> i(binary) : 방문한 도시들 / j(int) : i에서 방문한 도시들 중 마지막으로 방문한 도시(이게 있어야 다음 도시랑 연결할 수 있다.) / v = 비용
# 예시 : 도시 1, 2, 4를 방문했다면 i = 2 ** 1 + 2 ** 2 + 2 ** 4 = 22 / j는 1, 2, 4 가능 / v는 1, 2, 4를 방문하되, 마지막으로 j를 방문했을 때의 최소 비용
dp = {}
# 초기화. 첫 점 0만 방문했을 때(binary는 2 ** 0) last_city = 0, cost = 0,
# 시작점을 0으로 고정해도 괜찮다. 어차피 전부 순회할 수 있으니까 모든 경우 안봐도 됨. 결국에는 연결되니까
dp[1] = {0: 0} # 0만 방문한 상태니까 binary는 1. 시작점은 0. 비용은 0

# 0 이외에 방문할 도시 수를 하나씩 늘려가면서. dp 정복
for cnt in range(1, N):
    # 방문할 도시의 조합. 0은 이미 방문했으니 제외한다.
    cities_set = combinations(range(1, N), cnt)
    # 그 조합에 대해서, dp 업데이트
    for cities in cities_set:
        # 방문한 도시를 binary로 표현. 0은 항상 방문한 상태이므로, binary_cities는 1(2**0)로 시작
        binary_cities = 1
        # 도시들을 binary_cities에 반영
        for city in cities:
            binary_cities |= 1 << city
        # 초기화 해주고~
        dp[binary_cities] = {}
        # 도시마다 마지막으로 방문할 도시의 최소 비용을 계산한 후 dp에 업데이트
        for last_city in cities:
            # 마지막으로 방문할 도시만 빼고
            binary_cities_except_last_city = binary_cities ^ (1 << last_city)
            minimum_cost = float('inf')
            # 나머지 도시들을 돌면서 비용 계산
            for prev_last_city, prev_cost in dp[binary_cities_except_last_city].items():
                cost_to_last_city = costs[prev_last_city][last_city]
                # 갈 수 있는 길이 없다면 패스
                if cost_to_last_city == 0:
                    continue
                # 길이 있는 경우
                total_cost = prev_cost + cost_to_last_city
                minimum_cost = min(minimum_cost, total_cost)
            # minimum_cost가 그대로라면 마지막 도시로 갈 수 있는 길이 없다는 의미
            if minimum_cost < float('inf'):
                dp[binary_cities][last_city] = minimum_cost
                
# 이제 전부 방문한 애들에 대해서 마지막 점과 0을 이어주기
minimum_cost = (10 ** 6) * 17 + 1
for last_city, total_cost in dp[2 ** N - 1].items():
    if costs[last_city][0] == 0:
        continue
    minimum_cost = min(minimum_cost, total_cost + costs[last_city][0])
print(minimum_cost)