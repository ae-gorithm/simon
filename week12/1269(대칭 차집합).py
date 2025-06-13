NA, NB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(NA + NB - 2 * len(A & B))2