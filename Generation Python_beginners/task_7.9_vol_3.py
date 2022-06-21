a, b = int(input()), int(input())
res = {}
for i in range(a, b + 1):
    dividers = [j for j in range(1, i + 1) if i % j == 0]
    res.update({sum(dividers): i})
print(res[max(res)], max(res))
