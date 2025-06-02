N, M = map(int, input().split())
seq = list(map(int, input().split()))

"""
0.5초 안에 가능한 모든 수열의 합을 탐색해보는 것은 불가능할 것
모든 숫자가 '자연수'인 점을 착안, j를 증가시키면서 M을 초과하면 i를 증가시키면서 빼는 것이 어떨까
"""
cnt = 0
i = 0
cur_sum = 0

for j, s in enumerate(seq):
    cur_sum += s
    """
    여기서 구현해야할 로직
    1. cur_sum이 M과 같으면 cnt를 +하고 다음으로
    2. 작아도 다음으로
    3. 크면 같거나 작을때까지 빼고, 같으면 cnt를 +하고 다음으로
    
    => 크면 같거나 작을때까지 빼는 작업을 먼저 하고, 같으면 cnt를 +하는 방식으로 구현하면 되겠다.
    """
    while cur_sum > M:
        if i >= j: break
        cur_sum -= seq[i]
        i += 1
    
    if cur_sum == M:
        cnt += 1
        
print(cnt)