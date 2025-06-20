"""
일단 뭐 자르는건 어렵지 않고,
자른거에 대해 적용하면 되나? 재귀적으로?
그렇게 해보자.
"""
from functools import reduce

def get_set(matrix, r, c, step):
    part = [row[c:c+step] for row in matrix[r:r+step]]
    return reduce(lambda a, b: a.union(set(b)), part, set())

def check(matrix, r, c, step):
    global cnt
    e_set = get_set(matrix, r, c, step)
    if len(e_set) > 1:
        new_step = step // 3
        for next_r in range(r, r + step, new_step):
            for next_c in range(c, c + step, new_step):
                check(matrix, next_r, next_c, new_step)    
    else:
        index = e_set.pop() + 1
        cnt[index] += 1
        
N = int(input())
matrix = tuple(tuple(map(int, input().split())) for _ in range(N))
cnt = [0, 0, 0]
check(matrix, 0, 0, N)
print(*cnt, sep='\n')