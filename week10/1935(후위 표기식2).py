from operator import add, sub, mul, truediv
N = int(input())
"""
우선 후위 표기식이니까 스택을 활용해야 할 것 같다.
피연산자를 스택에 하나씩 넣고, 연산자를 만날때마다 두개 뽑고 계산 후 다시 스택에 push
연산자 우선순위는 어떻게 고려할 것인가
만약 ABC+*DE/-의 경우를 보자.
A*B+C-D/E 이렇게 된 식인데, 여기서 B+C를 먼저 계산을 해야하나?
일단 제출하고 보자.
"""
keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
value = dict()
ops = {'+': add, '-': sub, '*': mul, '/': truediv}
ops_keys = set(ops.keys())

exp = input()
for i in range(N):
    value[keys[i]] = int(input())
    
stack = []

for e in exp:
    if e in ops_keys:
        operand2 = stack.pop()
        operand1 = stack.pop()
        stack.append(ops[e](operand1, operand2))
    else:
        stack.append(value[e])
        
print(f'{stack[0]:.2f}')