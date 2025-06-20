"""
1일부터 N일까지 있다고 하자
N+1일에는 일을 마무리할 수 없다.
그럼 뭘 저장해야 할까? 그날까지 처리할 수 있는 최대 양이라고 생각하자. 그러면 저장할 때, 이틀 걸린다고 하면 하루 빼서 해야겠다.
"""

N = int(input())
max_pay = [0] * (N+1)

for i in range(1, N+1):
    T, P = map(int, input().split())
    flag = i + T - 1 > N
    cur_max = max(max_pay[:i])
    next_day = min(i + T - 1, N)
    pay = cur_max + (0 if flag else P)
    max_pay[next_day] = max(max_pay[next_day], pay)

print(max_pay[N])