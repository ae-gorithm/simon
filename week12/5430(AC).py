"""
그때그때 빼면 안된다. i와 j를 둬야한다. i:j를 하면 다 나오도록. 그리고 마지막에 결국 어디
"""

T = int(input())
for _ in range(T):
    func = input()
    n = input()
    arr = list(map(int, input().strip('[]').split(',')))
    s = 0
    e = n
    for i, d in enumerate(func.split('R')):
        s += len(d) if i % 2 == 0 else 0
        e -= len(d) if i % 2 == 1 else 0
        