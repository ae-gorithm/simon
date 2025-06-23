"""
그때그때 빼지말고 i:j를 하면 다 나오도록 해보자. 그리고 마지막에 결국 어디
"""

T = int(input())
for _ in range(T):
    func = input()
    n = int(input())
    arr = eval(input())
    step = [len(s) for s in func.split('R')]
    s = sum(e for i, e in enumerate(step) if i % 2 == 0)
    e = n - sum(e for i, e in enumerate(step) if i % 2 == 1)
    
    if s > e:
        print('error')
    else:
        result = arr[s:e]
        if len(step) % 2 == 0:
            result = result[::-1]
        print(f'[{",".join(map(str, result))}]')