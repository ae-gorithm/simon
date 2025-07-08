"""
와... 이거 발상의 전환
한 심사관이 특정 time 안에 처리할 수 있는 사람의 수 : time / t
그럼 그걸 줄여가면서, 딱 특정 사람의 수만 처리할 수 있는 "시간"을 찾아야겠네. 미쳤다
처음에는 가장 큰 걸로.
left와 right가 같을 때 까지인가?
종료 조건이 뭐지?
만약 total이 딱 맞게 떨어진다면? 근데 그거보다 작을 수도 있잖아? ㅇㅋ
"""
import sys

input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
left = 1
right = max(T) * M

while left < right:
    mid = (left + right) // 2
    total = sum(mid // t for t in T)

    if total >= M:
        right = mid
    else:
        left = mid + 1

print(left)