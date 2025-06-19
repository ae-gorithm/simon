"""
와우
그냥 상하좌우가 인접하다고하지 뭘 또
1. 학생을 정할 때, 일단 좋아하는 학생들이 어디있는지 파악해야 하니까 그 학생들의 위치는 갖고 있어야 한다.
2. 그 학생들의 인접한 칸들이 있을거고, 음... 인접에 인접이니까 이걸 어째야하지. 이게 관건이겠다.
3. 인접 카운트...?? 이건 또 어떻게 구하냐. 매번 설치할 때마다..와
3. 우선순위들이 있으니까 일단 그 순서대로 구현을 해보자.
"""
N = int(input())
favors = [None] * N

for _ in range(N):
    student, *favor = map(lambda x: int(x) - 1, input().split())
    favors[student] = favor

seats = [[None] * N for _ in N]
satisfied = [-1] * N

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def adjacent_seat(r, c):
    return tuple((r + x, c + y) for x, y in zip(dx, dy) if 0 <= r + x < N and 0 <= c + y < N)

def set_seat(student, r, c):
    seats[r][c] = student
    adjacent = adjacent_seat(r, c)
    for neighbor_student in adjacent:
        favors