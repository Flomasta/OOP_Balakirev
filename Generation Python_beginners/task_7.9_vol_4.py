n = int(input())
res = {}
for i in range(1, n + 1):
    dividers = [j for j in range(1, i + 1) if i % j == 0]
    res.update({i: len(dividers)})
print(*[f'{k}{"+" * v}' for k, v in res.items()], sep='\n')
