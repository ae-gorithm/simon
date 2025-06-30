"""
0부터 찾자.
그 앞에 있는 것들은 다 추월한 애들

"""

N = int(input())
Daekeun = dict()
for i in range(N):
    Daekeun[input()] = i

Youngsik = [Daekeun[input()] for _ in range(N)]
pass_index = 0
cnt = 0
passed = [False] * N

for seq in range(N):
    if passed[seq]:
        continue
    while True:
        next_car = Youngsik[pass_index]
        passed[next_car] = True
        pass_index += 1
        if next_car == seq:
            break
        cnt += 1

print(cnt)