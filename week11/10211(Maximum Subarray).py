"""
이거 지난번 투포인터?? 그거랑 비슷한 문제일 거 같은데.
일단 차이는 "정수형 배열"이다.
배열의 크기는 1000밖에 안되네.
근데 테스트 케이스가 몇개지?

투포인터로 갈 수 있나? 아닌 것 같은데
DP 문제라고 생각.
dp[i]는 뭘 담고 있어야하지? -> 현재까지의 MS는 반드시 들고 있어야 한다.
그리고 dp[i+1]을 구할 때는 뭐가 필요하지? -> i를 포함한 최대 합?을 갖고 있어야 한다. 그래야 i+1을 더했을 때 MS를 넘을지 안넘을지 판단할 수 있으니까
근데 i+1이 더 클 수도 있으니까 그것도 고려해주자
"""

T = int(input())
for _ in range(T):
    N = int(input())
    arr = tuple(map(int, input().split()))
    cur_sum, max_sum = arr[0], arr[0] 
    for e in arr[1:]:
        cur_sum = max(cur_sum + e, e)
        max_sum = max(max_sum, cur_sum)
    print(max_sum)