"""
문제 이해부터 하자...

1. 벨트는 회전한다. 내구도는 벨트 기준이다(컨베이어 벨트 X).
2. 로봇은 처음에 1~N까지 올릴 수 있다. 로봇이 이동하면 내구도는 감소한다.
2-1. 벨트가 회전하면서 컨베이어 벨트 내구도 감소? -> 내구도는 벨트 기준이므로 그대로.
3. 로봇은 1의 위치에만 에만 올릴 수 있다.

이동할 수 있다면 이동하고, 아니면 말고.

이제 구해야하는 것을 정리해보자.
1. 몇 단계를 진행중인지 파악하고 있어야 한다.
2. 로봇을 올리는 위치는 -단계
3. 로봇을 다음 칸으로 옮길 수 있는지 없는지 파악할 수 있어야 한다.
4. 올리면서 내구도 감소.

그러면 관리해야 하는 것
1. 내구도가 0이 된 칸의 수
2. 단계
3. 로봇들의 위치 -> 무엇으로 관리하는게 좋을까. 일단 List?
4. 이동하려는 칸에 로봇이 없다는 것은 어떻게 알 수 있지? -> 일단은 획기적인 방법이 안떠오르니까 그냥 한칸씩 밀자

이거 실제로 굴러가게 하는 게 낫겠다.
단계에 따라 벨트랑 맞추는게 나을듯
내구도도 같이 움직이면 되지 않나? -> 맞다.
"""
from collections import deque
N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([False] * N)

def rotate(belt, robots):
    belt.appendleft(belt.pop())
    robots.pop()
    robots.appendleft(False)
    robots[-1] = False
    return belt, robots

def put_robot(i, cnt, belt, robots):
    robots[i] = True
    belt[i] -= 1
    cnt += 1 if belt[i] == 0 else 0
    robots[-1] = False
    return cnt, belt, robots

def move_robot(i, j, cnt, belt, robots):
    if not robots[j] and belt[j] > 0:
        robots[i] = False
        cnt, belt, robots = put_robot(j, cnt, belt, robots)
    return cnt, belt, robots

cnt = 0
step = 0
while cnt < K:
    step += 1
    belt, robots = rotate(belt, robots)
    valid_robots = [(i, robot) for i, robot in enumerate(robots) if robot]
    for i, robot in reversed(valid_robots):
        cnt, belt, robots = move_robot(i, i+1, cnt, belt, robots)
    if belt[0] > 0:
        cnt, belt, robots = put_robot(0, cnt, belt, robots)
print(step)