lst = [3600, 60, 1]
final = []
n = int(input())
for i in lst:
    current = n // i
    final.append(str(current) if i == 3600 else str(current).zfill(2))
    n -= i * current
print(':'.join(final))
