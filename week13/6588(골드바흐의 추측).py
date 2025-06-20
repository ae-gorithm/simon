maximum = 10 ** 6
is_prime = [True] * (maximum + 1)

for i in range(3, int(maximum ** 0.5) + 1, 2):
    if not is_prime[i]:
        continue
    for j in range(i ** 2, maximum + 1, i):
        is_prime[j] = False

results = []
while even := int(input()):
    for odd in range(3, even // 2, 2):
        if is_prime[odd] and is_prime[even-odd]:
            results.append(f'{even} = {odd} + {even-odd}')
            break
print(*results, sep='\n')