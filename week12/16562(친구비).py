"""
안타까운 준석이
뭔가 DP 느낌이 난다. 가방안에 뭐 넣는 그런느낌? -> 아니다
연결이 되어 있으니까 그래프 일 것 같다.
친구 관계가 쭉 주어지니까, 그 사람이랑 친구를 하려면 생기는 최소비용?을 봐야할 것 같은데 -> 꼭 최소비용으로 하는건 아닐듯
각 노드별로 친구 될 수 있는 비용, 루트를 정리하고 있어야 하나?
일단 연결된 친구들을 구해야 할 것 같다.
돈 다 생길 때 까지.
우선 친구비는 최소 힙으로 구현하자.
근데 이게 최소 신장 트리 뭐 이런게 되나? -> 안될 것 같다. 가중치가 자꾸 바뀌니까
그래프 모양을 생각하자. 친구끼리는 가중치가 0인 것으로 되는거지
최소 신장 트리를 찾으면 될 것 같은데..? -> 보장할 수 있나? 이건 가중치가 0이 아닐때만 해당하는거 아닌가?
아니 잠깐만 친구의 친구는 친구라며
그러면 그냥 집합이 여러개 있는거잖아. 거기랑 이어지는 비용이 있는거고
복잡하게 생각할 필요가 없네
모두 각자의 set이 있다가 합치면 되는거네. 더 싼쪽으로. 그 친구들의 비용의 최소가 연결 비용 최소인거지. 이거 합치면 되겠다.
"""

JS = 0
N, M, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))

friends = [JS] * (N + 1)
for _ in range(M):
    i, j = map(int, input().split())
    
    while friends[i] != JS:
        i = friends[i]
    while friends[j] != JS:
        j = friends[j]
    if i == j:
        continue
    flag = cost[i] >= cost[j]
    friends[i if flag else j] = j if flag else i

minimum = sum(cost[i] for i in range(N + 1) if friends[i] == JS)
print(minimum if minimum <= k else 'Oh no')